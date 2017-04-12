from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Board, Group, Item
from .utils import parse_item_orders


class Index(generic.TemplateView):
    template_name = "task_manager/tracker.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        board = Board.objects.get(owner=self.request.user)
        context['board'] = board
        context['groups'] = Group.objects.filter(board=board)
        context['title'] = 'Task Tracker'
        return context


class AddGroup(generic.View):
    def post(self, request):
        g = Group()
        g.name = request.POST['group_name']  # TODO: use form to validate input
        board_id = int(request.POST['board_id'])
        board = get_object_or_404(Board, id=board_id)
        if not board.has_access(request.user):
            return HttpResponseForbidden()
        g.board = board
        g.order = g.get_next_order_id()
        g.save()
        return HttpResponseRedirect(reverse('index'))


class OrderGroup(generic.View):
    def post(self, request):
        order = 0
        item_ids = parse_item_orders(request.POST['items'])
        for item_id in item_ids:
            order += 1
            item = get_object_or_404(Item, id=item_id)
            if item.has_access(request.user):
                item.order = order
                item.save()
        return HttpResponse(status=200)


class AddItem(generic.View):
    def post(self, request):
        item = Item()
        group_id = int(request.POST['group_id'])
        group = get_object_or_404(Group, id=group_id)
        if not group.has_access(request.user):
            return HttpResponseForbidden()
        item.group = group
        item.order = item.get_next_order_id()
        item.content = request.POST['content']  # TODO: validate content with form?
        item.save()
        return HttpResponseRedirect(reverse('index'))


class MoveItem(generic.View):
    def post(self, request):
        item_id = int(request.POST['item_id'])
        new_group_id = int(request.POST['group_id'])
        new_group = get_object_or_404(Group, id=new_group_id)
        item = get_object_or_404(Item, id=item_id)
        if not item.has_access(request.user) or not new_group.has_access(request.user):
            return HttpResponseForbidden()

        item.group_id = new_group_id
        item.save()
        return HttpResponse(status=200)


class Login(generic.TemplateView):
    template_name = "task_manager/login.html"

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['title'] = 'Task Tracker'
        return context

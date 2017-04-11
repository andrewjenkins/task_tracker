from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
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
        g.order = Group.get_next_order_id()
        g.name = request.POST['group_name']  # TODO: use form to validate input
        g.board_id = int(request.POST['board_id'])  # TODO: validate that user owns board
        g.save()
        return HttpResponseRedirect(reverse('index'))


class AddItem(generic.View):
    def post(self, request):
        item = Item()
        item.group_id = request.POST['group_id'] # TODO: validate that user owns group
        item.order = item.get_next_order_id()
        item.content = request.POST['content']
        item.save()
        return HttpResponseRedirect(reverse('index'))


class OrderItems(generic.View):
    def post(self, request):
        # TODO: validate that items exist and user owns item
        order = 0
        item_ids = parse_item_orders(request.POST['items'])
        for item_id in item_ids:
            order += 1
            item = Item.objects.get(id=item_id)
            item.order = order
            item.save()
        return HttpResponse(status=200)


class MoveItem(generic.View):
    def post(self, request):
        # TODO: validate that items exist and user owns item/groups
        item_id = int(request.POST['item_id'])
        group_id = int(request.POST['group_id'])
        item = Item.objects.get(id=item_id)
        item.group_id = group_id
        item.save()
        return HttpResponse(status=200)


class Login(generic.TemplateView):
    template_name = "task_manager/login.html"

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['title'] = 'Task Tracker'
        return context

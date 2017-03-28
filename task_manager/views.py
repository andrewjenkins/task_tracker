from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Board, Group, Item


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
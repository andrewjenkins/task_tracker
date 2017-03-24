from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Board, Group, Item


class IndexView(generic.TemplateView):
    template_name = "task_manager/tracker.html"

    def get_context_data(self, **kwargs):
        board = Board.objects.get(owner=self.request.user)
        groups = Group.objects.get(board=board)
        context = {
            'title': "tester",
            'groups': groups
        }
        return context

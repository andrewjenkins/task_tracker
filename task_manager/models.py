from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    owner = models.ForeignKey(User)


class Group(models.Model):
    name = models.CharField(max_length=64)
    board = models.ForeignKey(Board)


class Item(models.Model):
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

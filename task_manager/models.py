from django.db import models


class Board(models.Model):
    owner = models.ForeignKey()


class Group(models.Model):
    name = models.CharField(max_length=64)
    board = models.ForeignKey(Board)


class Item(models.Model):
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

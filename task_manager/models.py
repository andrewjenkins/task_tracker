from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User)


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField()
    name = models.CharField(max_length=64)
    board = models.ForeignKey(Board)

    def __str__(self):
        return self.name

    @staticmethod
    def get_next_order_id():
        return Group.objects.count() + 1

    class Meta:
        ordering = ['order']


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField()
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['order']

    @staticmethod
    def get_next_order_id():
        return Item.objects.count() + 1

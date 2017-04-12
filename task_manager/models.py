from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)

    def has_access(self, user):
        return self.owner == user


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField()
    name = models.CharField(max_length=64)
    board = models.ForeignKey(Board)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)

    def has_access(self, user):
        return self.board.has_access(user)

    def __str__(self):
        return self.name

    def get_next_order_id(self):
        return self.board.group_set.count() + 1

    class Meta:
        ordering = ['order']


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField()
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)

    def has_access(self, user):
        return self.group.has_access(user)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['order']

    def get_next_order_id(self):
        return self.group.item_set.count() + 1

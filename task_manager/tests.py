from unittest import mock
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Board, Group, Item


class BoardMethodTests(TestCase):
    def test_has_owner_positive(self):
        user = User()
        board = Board(owner=user)

        result = board.has_access(user)

        self.assertTrue(result)

    def test_has_owner_negative(self):
        user_owner = User()
        board = Board(owner=user_owner)
        user_other = User()

        result = board.has_access(user_other)

        self.assertFalse(result)

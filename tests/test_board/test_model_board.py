import pytest
from django.test import TestCase
from goals.models import Board



@pytest.mark.django_db
class BoardTest(TestCase):

    def create_board(self, title="Board object", is_deleted=False):
        return Board.objects.create(title=title, is_deleted=is_deleted)

    def test_board_creation(self):
        w = self.create_board()
        self.assertTrue(isinstance(w, Board))

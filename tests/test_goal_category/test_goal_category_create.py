import pytest
from django.urls import reverse
from freezegun import freeze_time

from goals.models import BoardParticipant
from tests.factories import BoardParticipantFactory


@pytest.mark.django_db
class TestGoalCategoryCreate:
    url = reverse('goals:create-goalcategory')

    def test_not_authorized(self, client, faker):
        response = client.post(self.url, {"title": faker.text(20)})
        assert response.status_code == 403

    def test_create_category_by_board_reader(self, auto_login_user, create_board, user, faker):
        # Создали доску для пользователя user
        board, owner = create_board(owner=user)

        # Залогинились под пользователем board_owner
        client, board_reader = auto_login_user()

        # Добавим к доске board участника board_reader c правом на чтение
        BoardParticipantFactory.create(
            user=board_reader,
            board=board,
            role=BoardParticipant.Role.reader
        )

        response = client.post(self.url, {
            "title": faker.text(20),
            "board": board.id,
        })
        assert response.status_code == 400

    def test_create_category_by_board_writer(self, auto_login_user, create_board, user, faker):
        # Создали доску для пользователя user
        board, owner = create_board(owner=user)

        # Залогинились под пользователем board_owner
        client, board_writer = auto_login_user()

        # Добавим к доске board участника board_reader c правом на чтение
        BoardParticipantFactory.create(
            user=board_writer,
            board=board,
            role=BoardParticipant.Role.writer
        )

        response = client.post(self.url, {
                "title": faker.text(20),
                "board": board.id,
        })
        assert response.status_code == 201

        # Видим ошибку из GoalCategoryCreateSerializer
        # assert response.json() == {'board': ['Please check role']}

    @freeze_time('1970-01-01T00:00:00')
    def test_success(self, auto_login_user, create_board):
        client, user = auto_login_user()

        board, _ = create_board(owner=user)

        response = client.post(self.url, {
            "title": "new_cat_title",
            "board": board.id,
        })

        assert response.status_code == 201
        assert response.data == {
            "id": 2,
            "created": '1970-01-01T00:00:00Z',
            "updated": '1970-01-01T00:00:00Z',
            "title": "new_cat_title",
            "is_deleted": False,
            "board": board.id
        }
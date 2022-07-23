import pytest

from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db
class TestBoardList:
    url = reverse('goals:list-board')

    @freeze_time('1970-01-01T05:00:00')
    def test_success(self, auto_login_user, board):
        client, _ = auto_login_user()

        # data = {
        #     "id": board.id,
        #     "created": "2022-07-04T09:01:31.575766Z",
        #     "updated": "2022-07-04T09:17:49.783309Z",
        #     "title": board.title,
        #     "is_deleted": False
        # }

        response = client.get(self.url, content_type='application/json')

        assert response.status_code == 200
        assert response.json() == {
            "id": board.id,
            "created": "2022-07-04T09:01:31.575766Z",
            "updated": "2022-07-04T09:17:49.783309Z",
            "title": board.title,
            "is_deleted": False
        }
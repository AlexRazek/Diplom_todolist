import pytest
from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db
class TestBoardCreate:
    url = reverse('goals:create-board')

    @freeze_time('1970-01-01T05:00:00')
    def test_success(self, auto_login_user, board):
        client, _ = auto_login_user()

        response = client.post(self.url, {
            "title": board.title,
        })

        assert response.status_code == 201
        assert response.data == {
            "id": board.id+1,
            "created": '1970-01-01T05:00:00Z',
            "updated": '1970-01-01T05:00:00Z',
            "title": board.title,
            "is_deleted": False
        }


    def test_failed_not_authorized(self, client, board):
        response = client.post(self.url, {
            "title": board.title,
        })

        assert response.status_code == 403
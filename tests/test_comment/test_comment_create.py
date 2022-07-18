import pytest
from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db
class TestCommentCreate:
    url = reverse('goals:create-goalcomment')

    @freeze_time('1970-01-01T05:00:00')
    def test_success(self, auto_login_user):
        client, _ = auto_login_user()

        response = client.post(self.url, {
            "text": "New moments",
            "goal": 1
        })

        assert response.status_code == 201
        assert response.data == {
            "id": 2,
            "created": '1970-01-01T05:00:00Z',
            "updated": '1970-01-01T05:00:00Z',
            "text": "New moments",
            "goal": 1,
            "user": 3,
        }

    def test_failed_not_authorized(self, client):
        response = client.post(self.url, {
            "text": "New moments",
            "goal": 1,
        })

        assert response.status_code == 403

import pytest
from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db
class TestGoalCreate:
    url = reverse('goals:create-goal')

    @freeze_time('1970-01-01T05:00:00')
    def test_success(self, auto_login_user):
        client, _ = auto_login_user()

        response = client.post(self.url, {
            "title": "Letter",
            "description": "New writer",
            "status": 1,
            "priority": 2,
            "category": 3
        })

        assert response.status_code == 201
        assert response.data == {
            "id": 1,
            "created": '1970-01-01T05:00:00Z',
            "updated": '1970-01-01T05:00:00Z',
            "title": "Letter",
            "description": "writer",
            "status": 1,
            "priority": 2,
            "due_date": '1970-01-01T05:00:00Z',
            "category": 3,
        }



    def test_failed_not_authorized(self, client):
        response = client.post(self.url, {
            "title": "Letter",
            "description": "New writer",
            "status": 1,
            "priority": 2,
            "category": 3
        })

        assert response.status_code == 403


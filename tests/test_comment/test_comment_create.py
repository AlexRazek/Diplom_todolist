import pytest
# from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db
class TestCommentCreate:
    url = reverse('goals:create-goalcomment')

    def test_failed_not_authorized(self, client):
        response = client.post(self.url, {
            "text": "New moments",
            "goal": 1,
        })

        assert response.status_code == 403

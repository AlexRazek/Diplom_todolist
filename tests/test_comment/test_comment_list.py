import pytest


from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db
class TestGaolCommentList:
    url = reverse('goals:list-goalcomment')

    @freeze_time('1970-01-01T05:00:00')
    def test_success(self, auto_login_user):
        client, _ = auto_login_user()

        response = client.get(self.url)

        assert response.status_code == 200
        assert response.json() == []
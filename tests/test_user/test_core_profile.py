import pytest
# from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db
class TestCoreProfileRead:
    url = reverse('core:profile')

    def test_core_failed_not_authorized(self, client):
        response = client.get(self.url)
        assert response.status_code == 403

    def test_core_profile_read(self, auto_login_user):
        client, _ = auto_login_user()

        response = client.get(self.url)

        assert response.status_code == 200
        # assert response.data == {
        #     "id": 1,
        #     "username": "",
        #     "first_name": "",
        #     "last_name": "",
        #     "email": ""
        # }


@pytest.mark.django_db
class TestCoreProfile:
    url = reverse('core:profile')

    def test_core_profile_put(self, auto_login_user):
        client, _ = auto_login_user()

        response = client.patch(self.url, {
            "username": "kik"
        })

        assert response.status_code == 200
        assert response.data == {
            "id": 1,
            "username": "kik",
            "first_name": "",
            "last_name": "",
            "email": ""
        }

    def test_core_profile_delete(self, auto_login_user):
        client, _ = auto_login_user()

        response = client.delete(self.url, {
            "id": 1,
            "username": "Alex"
        })

        assert response.status_code == 200
        assert response.data == {}


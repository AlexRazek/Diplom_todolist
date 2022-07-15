import pytest
from django.urls import reverse
from freezegun import freeze_time

from todolist.test import BaseAPITestCase
# from core.urls import login


class LoginTestCase(BaseAPITestCase):
    url = reverse('core:login')

    @pytest.mark.django_db
    @freeze_time('1970-01-01T05:00:00')
    def test_success_login(self):
        assert self.user.last_login is None
        response = self.client.post(self.url, {
            'username': self.user.username,
            'password': self._user_password
        })
        assert response.status_code == 200
        assert response.json() == {
            'email': self.user.email,
            'first_name': self.user.first_name,
            'id': self.user.id,
            'last_name': self.user.last_name,
            'username': self.user.username,
        }
        assert 'sessionid' in self.client.cookies

        self.user.refresh_from_db()
        assert self.user.last_login is not None and self.user.last_login.isoformat() == '1970-01-01T05:00:00+00:00'

    def test_user_not_found(self):
        response = self.client.post(self.url, {
            'username': self._faker.user_name(),
            'password': self._faker.password(special_chars=False, length=12)
        })
        assert response.status_code == 403
        assert 'sessionid' not in self.client.cookies

    def test_invalid_password(self):
        response = self.client.post(self.url, {
            'username': self.user.username,
            'password': self._faker.password()
        })
        assert response.status_code == 403
        assert 'sessionid' not in self.client.cookies

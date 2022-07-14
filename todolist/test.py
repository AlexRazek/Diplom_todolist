from faker import Faker
from rest_framework.test import APITestCase

from tests.factories import UserFactory


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self._faker = Faker()
        self._user_password = self._faker.password()
        self.user = UserFactory.create()
        self.user.set_password(self._user_password)
        self.user.save()

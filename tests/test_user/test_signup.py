import pytest
from django.test import TestCase
from django.urls import reverse

from core.models import User


@pytest.mark.django_db
class TestSignUp(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1', email='user1@gmail.com', password='1234'
        )
        self.data = {
            'username': 'test',
            'email': 'test@hotmail.com',
            'password1': 'test12345',
            'password2': 'test12345'

        }

    def test_new_user_is_registered(self):
        nb_old_users = User.objects.count()
        self.client.post(reverse('core:login'), self.data)
        nb_new_users = User.objects.count()

        self.assertEqual(nb_new_users, nb_old_users)

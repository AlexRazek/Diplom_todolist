import pytest
import uuid


@pytest.fixture()
@pytest.mark.django_db
def hr_token(client, django_user_model):
    username = "username"
    password = "password"

    django_user_model.objects.create_user(username=username, password=password)
    response = client.post("/core/login", {"username": username, "password": password}, format='json')

    assert response.status_code == 200
    return response


@pytest.fixture()
def test_password():
    return 'strong-test-pass'


@pytest.fixture()
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture()
@pytest.mark.django_db
def auto_login_user(db, client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user

    return make_auto_login

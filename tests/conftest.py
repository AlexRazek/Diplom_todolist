import uuid
import pytest

from pytest_factoryboy import register
from core.models import User
from tests.factories import BoardParticipantFactory, UserFactory, GoalCategoryFactory, BoardFactory, GoalFactory, GoalCommentFactory

pytest_plugins = "tests.fixtures"

register(BoardFactory)
register(GoalFactory)
register(GoalCategoryFactory)
register(UserFactory)
register(BoardParticipantFactory)
register(GoalCommentFactory)


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


@pytest.fixture()
@pytest.mark.django_db
def create_board(db):
    def _create_board(owner: User):
        board_participants = BoardParticipantFactory.create(user=owner)
        return board_participants.board, board_participants.user

    return _create_board


@pytest.fixture()
@pytest.mark.django_db
def create_category(db):
    def _create_category(user: User):
        goal_categories = GoalCategoryFactory.create(user=user)
        return goal_categories

    return _create_category


@pytest.fixture()
@pytest.mark.django_db
def user():
    return UserFactory.create()

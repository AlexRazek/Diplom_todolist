import factory.django

from core.models import User
from goals.models import Board, BoardParticipant, GoalCategory, Goal


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True

    class Meta:
        model = User


class BoardFactory(factory.django.DjangoModelFactory):
    title = factory.sequence(lambda n: f'board_title_{n}')
    is_deleted = False

    class Meta:
        model = Board


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)
    role = BoardParticipant.Role.owner

    class Meta:
        model = BoardParticipant


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    board = factory.SubFactory(BoardFactory)
    title = factory.sequence(lambda n: f'goalcategory_title_{n}')
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = GoalCategory


class GoalFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    title = factory.Faker('title')
    description = factory.Faker('New description')
    category = factory.SubFactory(GoalCategoryFactory)
    status = factory.Faker('1')
    priority = factory.Faker('2')
    due_date = '1970-01-01T05:00:00Z'

    class Meta:
        model = Goal

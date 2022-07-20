# from factory.django import DjangoModelFactory
import factory.django

from core.models import User
from goals.models import Goal, Board, GoalCategory, GoalComment


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True

    class Meta:
        model = User


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker("board_test")
    user = factory.SubFactory(UserFactory)


class BoardParticipant(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    role = factory.Faker("2")
    user = factory.SubFactory(UserFactory)


class BoardFactoryPk(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker("board_pk_test")
    participants = factory.SubFactory(BoardParticipant)


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory

    board = factory.Faker("board_test")
    title = factory.Faker("title_test")
    user = factory.SubFactory(UserFactory)


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    category = factory.Faker("category")
    title = factory.Faker("title_goal")
    user = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalComment

    goal = factory.SubFactory(GoalFactory)
    text = factory.Faker("New moments")
    user = factory.Faker(2)
    category = factory.SubFactory(GoalCategoryFactory)
    board = factory.Faker(2)

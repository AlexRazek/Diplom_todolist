from datetime import date

import factory.django

from core.models import User
from goals.models import Board, BoardParticipant, GoalCategory, Goal, GoalComment


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
    title = factory.sequence(lambda n: f'goal_title_{n}')
    description = factory.sequence(lambda n: f'goal_description_{n}')
    category = factory.SubFactory(GoalCategoryFactory)
    status = factory.sequence(lambda n: f'{n}')
    priority = factory.sequence(lambda n: f'{n}')
    due_date = date.today().strftime('%Y-%m-%d')

    class Meta:
        model = Goal


class GoalCommentFactory(factory.django.DjangoModelFactory):
    goal = factory.SubFactory(GoalFactory)
    text = factory.sequence(lambda n: f'goalcomment_text_{n}')
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = GoalComment


import factory.django

from core.models import User
from goals.models import Board, BoardParticipant


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

    class Meta:
        model = Board


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)
    role = BoardParticipant.Role.owner

    class Meta:
        model = BoardParticipant

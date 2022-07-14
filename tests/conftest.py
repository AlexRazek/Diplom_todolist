from pytest_factoryboy import register

from tests.factories import BoardFactory, UserFactory, GoalCategoryFactory, GoalFactory, BoardParticipant, \
    BoardFactoryPk

#Fixtures
pytest_plugins = "tests.fixtures"


#Factories
register(BoardFactory)
register(BoardFactoryPk)
register(BoardParticipant)
register(UserFactory)
register(GoalCategoryFactory)
register(GoalFactory)

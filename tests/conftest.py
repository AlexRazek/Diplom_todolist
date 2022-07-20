from pytest_factoryboy import register

from tests.factories import BoardFactory, BoardFactoryPk, BoardParticipant, UserFactory, GoalCategoryFactory, GoalFactory, CommentFactory

#Fixtures
pytest_plugins = "tests.fixtures"


#Factories
register(BoardFactory)
register(BoardFactoryPk)
register(BoardParticipant)
register(UserFactory)
register(GoalCategoryFactory)
register(GoalFactory)
register(CommentFactory)

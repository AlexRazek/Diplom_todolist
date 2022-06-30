from django.urls import path

from goals.views import category, goals, comment, boards

urlpatterns = [
    path("goal_category/create", category.GoalCategoryCreateView.as_view()),
    path("goal_category/list", category.GoalCategoryListView.as_view()),
    path("goal_category/<pk>", category.GoalCategoryView.as_view()),

    path("goal/create", goals.GoalCreateView.as_view()),
    path("goal/list", goals.GoalListView.as_view()),
    path("goal/<pk>", goals.GoalView.as_view()),

    path("goal_comment/create", comment.CommentCreateView.as_view()),
    path("goal_comment/list", comment.CommentListView.as_view()),
    path("goal_comment/<pk>", comment.CommentView.as_view()),

    path("boards/create", boards.BoardCreateView.as_view(), name='create'),
    path("boards/list", boards.BoardListView.as_view(), name='list'),
    path("boards/<pk>", boards.BoardView.as_view(), name='main'),
]
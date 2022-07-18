from django.urls import path

from goals.views import category, goals, comment, boards

urlpatterns = [
    path("goal_category/create", category.GoalCategoryCreateView.as_view(), name='create-goalcategory'),
    path("goal_category/list", category.GoalCategoryListView.as_view(), name='list-goalcomment'),
    path("goal_category/<pk>", category.GoalCategoryView.as_view(), name='pk-goalcomment'),

    path("goal/create", goals.GoalCreateView.as_view(), name='create-goal'),
    path("goal/list", goals.GoalListView.as_view(), name='list-goal'),
    path("goal/<pk>", goals.GoalView.as_view(), name='pk-goal'),

    path("goal_comment/create", comment.CommentCreateView.as_view(), name='create-goalcomment'),
    path("goal_comment/list", comment.CommentListView.as_view(), name='list-goalcomment'),
    path("goal_comment/<pk>", comment.CommentView.as_view(), name='pk-goalcomment'),

    path("board/create", boards.BoardCreateView.as_view(), name='create-board'),
    path("board/list", boards.BoardListView.as_view(), name='list-board'),
    path("board/<pk>", boards.BoardView.as_view(), name='pk-board'),
]
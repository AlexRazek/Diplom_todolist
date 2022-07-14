from datetime import datetime

import pytest

# from goals.models import GoalCategory, User
# from goals.serializers import GoalCategorySerializer
from goals.views.goals import GoalListView
from tests.factories import GoalFactory


@pytest.mark.django_db
def test_goal_category_list(client, hr_token):
    goals = GoalFactory.create_batch(10)

    expected_response = {
        "count": 10,
        "next": None,
        "previous": None,
        "results": GoalListView(goals, many=True).data
    }

    response = client.get(
        f"goals/goal_category/list/",
        content_type="application/json",
        HTTP_AUTHORIZATION="Token " + hr_token)

    assert response.status_code == 200
    assert response.data == expected_response

# @pytest.mark.django_db
# def test_goal_category_list(client, hr_token):
#     expected_response = {
#         "count": 0,
#         "next": "string",
#         "previous": "string",
#         "results": [
#             {
#                 "id": 1,
#                 "user": {
#                     "id": 2,
#                     "username": "Nik",
#                     "first_name": "string",
#                     "last_name": "string",
#                     "email": "Nik@google.com"
#                 },
#                 "created": datetime.now().strftime("%Y-%m-%d"),
#                 "updated": datetime.now().strftime("%Y-%m-%d"),
#                 "title": "New",
#                 "is_deleted": True,
#                 "board": 3
#             }
#         ]
#     }
#     goal_categories = GoalCategoryFactory.create_batch(10)
#
#     expected_response = {
#         "count": 10,
#         "next": None,
#         "previous": None,
#         "results": GoalCategoryListView(goal_categories, many=True).data
#     }
#

#     response = client.get(
#         "/goal_category/list/",
#         content_type="application/json",
#         HTTP_AUTHORIZATION="Token " + hr_token)
#
#     assert response.status_code == 200
#     assert response.data == expected_response


# @pytest.mark.django_db
# def test_goal_category_list(client):
#     goal_category = GoalCategory.objects.create(
#         title="что-то интересное",
#         is_deleted=False,
#     )
#     expected_response = {
#         "id": goal_category.pk,
#         "user": {
#             "id": 1,
#             "username": "None",
#             "first_name": "",
#             "last_name": "",
#             "email": ""
#         },
#         "created": datetime.now().strftime("%Y-%m-%d"),
#         "updated": datetime.now().strftime("%Y-%m-%d"),
#         "title": "что-то интересное",
#         "is_deleted": False,
#         "board": 2
#         }
#
#     response = client.get("goal_category/create/")
#
#     assert response.status_code == 200
#     assert response.data == expected_response

# # from datetime import date
from datetime import datetime

import pytest
from freezegun import freeze_time


@pytest.mark.django_db
@freeze_time('1970-01-01T05:00:00')
def test_goal_category_create(client, hr_token):

    data = {
        "title": "Ludovik",
        "board": 1
    }

    response = client.post(
        "/goals/goal_category/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer{hr_token}")

    assert response.status_code == 200
    assert response.data == {
        "id": 1,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "title": "Ludovik",
        "is_deleted": False,
        "board": 1
    }

#
# @pytest.mark.django_db
# def test_goal_category_create(client, hr_token):
#     expected_response = {
#         "board": 1,
#         "title": "Popular things",
#         "user": 1,
#         "is_deleted": False,
#     }
#
#     data = {
#         "title": "Popular things"
#     }
#
#     response = client.post(
#         "/goal_category/create/", data,
#         content_type="application/json", HTTP_AUTHORIZATION="Token " + hr_token)
#
#     assert response.status_code == 201
#     assert response.data == expected_response
#

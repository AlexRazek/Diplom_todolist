from datetime import datetime

import pytest
from freezegun import freeze_time


@pytest.mark.django_db
@freeze_time('1970-01-01T05:00:00')
def test_goal_category_create(client, hr_token):

    data = {
          "title": "Letter",
          "description": "New writer",
          "status": 1,
          "priority": 2,
          "category": 3
    }

    response = client.post(
        "/goals/goal/create",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer{hr_token}")

    assert response.status_code == 200
    assert response.data == {
            "id": 1,
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d"),
            "title": "Letter",
            "description": "writer",
            "status": 1,
            "priority": 2,
            "due_date": datetime.now().strftime("%Y-%m-%d"),
            "category": 3
        }

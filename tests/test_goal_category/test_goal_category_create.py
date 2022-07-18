from datetime import datetime

# import pytest
# from freezegun import freeze_time

import pytest
from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db
class TestGoalCategoryCreate:
    url = reverse('goals:create-goalcategory')

    @freeze_time('1970-01-01T05:00:00')
    def test_success(self, auto_login_user):
        client, _ = auto_login_user()

        response = client.post(self.url, {
            "title": "Ludovik",
            "board": 1,
        })

        assert response.status_code == 201
        assert response.data == {
            "id": 10,
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d"),
            "title": "Ludovik",
            "is_deleted": False,
            "board": 1
        }



    def test_failed_not_authorized(self, client):
        response = client.post(self.url, {
            "title": "Ludovik",
        })

        assert response.status_code == 403


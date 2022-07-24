import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestGoalCategoryList:
    url = reverse('goals:list-goalcategory')

    def test_not_authorized(self, client):
        response = client.get(self.url)
        assert response.status_code == 403

    def test_category_is_deleted(self, client, board_participant, goal_category):
        goal_category.is_deleted = True
        goal_category.save(update_fields=('is_deleted',))

        client.force_login(user=board_participant.user)
        response = client.get(self.url)
        assert response.status_code == 200
        assert response.json() == []

    def test_success(self, client, board_participant, goal_category):
        client.force_login(user=board_participant.user)
        response = client.get(self.url)
        assert response.status_code == 200
        assert response.json() == [
            {
                'id': goal_category.id,
                'user': {
                    'id': board_participant.user.id,
                    'username': board_participant.user.username,
                    'first_name': board_participant.user.first_name,
                    'last_name': board_participant.user.last_name,
                    'email': board_participant.user.email
                },
                'created': goal_category.created.isoformat().replace('+00:00', 'Z'),
                'updated': goal_category.updated.isoformat().replace('+00:00', 'Z'),
                'title': goal_category.title,
                'is_deleted': False,
                'board': goal_category.board_id
            }
        ]
import pytest

from django.urls import reverse


@pytest.mark.django_db
class TestGoalCommentList:
    url = reverse('goals:list-goalcomment')

    def test_not_authorized(self, client):
        response = client.get(self.url)
        assert response.status_code == 403

    def test_success(self, client, goal_comment, board_participant):
        client.force_login(user=board_participant.user)
        response = client.get(self.url)

        assert response.status_code == 200
        assert response.json() == [
            {
                'id': goal_comment.id,
                'user': {
                    'id': board_participant.user.id,
                    'username': board_participant.user.username,
                    'first_name': board_participant.user.first_name,
                    'last_name': board_participant.user.last_name,
                    'email': board_participant.user.email
                },
                'created': goal_comment.created.isoformat().replace('+00:00', 'Z'),
                'updated': goal_comment.updated.isoformat().replace('+00:00', 'Z'),
                'text': goal_comment.text,
                'goal': goal_comment.goal_id,
            }
        ]

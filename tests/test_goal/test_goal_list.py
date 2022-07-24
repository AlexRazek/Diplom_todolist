import ast

import pytest

from django.urls import reverse


@pytest.mark.django_db
class TestGoalList:
    url = reverse('goals:list-goal')

    def test_not_authorized(self, client):
        response = client.get(self.url)
        assert response.status_code == 403

    def test_success(self, client, goal, board_participant):
        client.force_login(user=board_participant.user)
        response = client.get(self.url)

        assert response.status_code == 200
        assert response.json() == [
            {
                'id': goal.id,
                'user': {
                    'id': board_participant.user.id,
                    'username': board_participant.user.username,
                    'first_name': board_participant.user.first_name,
                    'last_name': board_participant.user.last_name,
                    'email': board_participant.user.email
                },
                'created': goal.created.isoformat().replace('+00:00', 'Z'),
                'updated': goal.updated.isoformat().replace('+00:00', 'Z'),
                'title': goal.title,
                'description': goal.description,
                'status': ast.literal_eval(goal.status),
                'priority': ast.literal_eval(goal.priority),
                'due_date': goal.due_date,
                'category': goal.category_id
            }
        ]

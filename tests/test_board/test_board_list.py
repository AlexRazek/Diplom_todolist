import pytest

from django.urls import reverse


@pytest.mark.django_db
class TestBoardList:
    url = reverse('goals:list-board')

    def test_not_authorized(self, client):
        response = client.get(self.url)
        assert response.status_code == 403

    def test_success(self, client, board, board_participant):
        client.force_login(user=board_participant.user)
        response = client.get(self.url)

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": board.id,
                "created": board.created.isoformat().replace('+00:00', 'Z'),
                "updated": board.updated.isoformat().replace('+00:00', 'Z'),
                "title": board.title,
                "is_deleted": False
            }
        ]
import pytest
from freezegun import freeze_time
from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestBoardRetrieveUpdateDestroy:
    # url = f"goals/board/{board.id}"
    # url = reverse('goals:pk-board')
    url = f'goals/board/<pk>'

    # @freeze_time('1970-01-01T05:00:00')
    def test_board_pk(self, auto_login_user):
        client, _ = auto_login_user()
        response = client.delete(self.url, {
            "id": 1,
        })

        assert response.status_code == 204

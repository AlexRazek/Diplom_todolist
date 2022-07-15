import pytest
from datetime import datetime
from goals.serializers import BoardParticipantSerializer
from tests.factories import BoardFactoryPk


@pytest.mark.django_db
def test_board_list(client, hr_token):
    # boards = BoardFactoryPk.create_batch(10)

    expected_response = {
        "id": 10,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "title": "string",
        "is_deleted": False,
        "participants": BoardParticipantSerializer(many=True).data
    }

    response = client.get(
        "/goals/board/{}/".format(1),
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer{hr_token}")

    assert response.status_code == 200
    assert response.data == expected_response

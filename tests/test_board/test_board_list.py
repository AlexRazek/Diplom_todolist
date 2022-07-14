import pytest

from goals.serializers import BoardListSerializer
from tests.factories import BoardFactory


@pytest.mark.django_db
def test_board_list(client, hr_token):
    boards = BoardFactory.create_batch(10)

    # expected_response = {
    #     "count": 10,
    #     "next": None,
    #     "previous": None,
    #     # "results": BoardListSerializer(boards, many=True).data
    # }

    response = client.get(
        f"/goals/board/list/",
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer{hr_token}")

    assert response.status_code == 200
    assert response.data == BoardListSerializer(boards, many=True).data

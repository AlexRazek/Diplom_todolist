import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_view_unauthorized(client):
    url = reverse('social')
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_view_as_admin(admin_client):
    url = reverse('admin')
    response = admin_client.get(url)
    assert response.status_code == 200

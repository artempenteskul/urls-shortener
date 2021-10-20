import pytest

from django.urls import reverse
from django.contrib.auth.models import User

from .models import Url


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def url_create():
    return Url.objects.create(url='https://www.youtube.com/')


@pytest.mark.django_db
def test_get_url_list(api_client, url_create):
    url = reverse('shortener:url-list')
    response = api_client.get(url)
    assert response.status_code == 200, 'Unexpected status code'
    assert response['content-type'] == 'application/json', 'Unexpected content-type'
    assert Url.objects.count() == 1, 'Unexpected objects quantity'


@pytest.mark.django_db
def test_create_url(api_client):
    user = User.objects.create_user(username='artem', password='artem123')
    url = reverse('shortener:short-url', kwargs={'full_url': 'https://www.youtube.com/'})
    api_client.force_authenticate(user=user)
    response = api_client.post(url)
    assert response.status_code == 200, 'Unexpected status code'
    assert response['content-type'] == 'application/json', 'Unexpected content-type'
    assert Url.objects.count() == 1, 'Unexpected objects quantity'


@pytest.mark.django_db
def test_unauthenticated_create_url(api_client):
    url = reverse('shortener:short-url', kwargs={'full_url': 'https://www.youtube.com/'})
    response = api_client.post(url)
    assert response.status_code == 403, 'Unexpected status code'


@pytest.mark.django_db
def test_get_redirect_url(api_client, url_create):
    url1 = url_create
    url = reverse('shortener:url-redirect', kwargs={'url_hash': url1.url_hash})
    response = api_client.get(url)
    assert response.status_code == 302, 'Unexpected status code'
    assert response['content-type'] == 'text/html; charset=utf-8', 'Unexpected content-type'


@pytest.mark.django_db
def test_get_url_count(api_client, url_create):
    url = reverse('shortener:url-count')
    response = api_client.get(url)
    assert response.status_code == 200, 'Unexpected status code'
    assert response['content-type'] == 'application/json', 'Unexpected content-type'
    assert response.data == {'urls_count': 1}, 'Unexpected response data'


@pytest.mark.django_db
def test_get_url_popular(api_client, url_create):
    url = reverse('shortener:urls-popular')
    response = api_client.get(url)
    assert response.status_code == 200, 'Unexpected status code'
    assert response['content-type'] == 'application/json', 'Unexpected content-type'

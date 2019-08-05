import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

User = get_user_model()


@pytest.mark.django_db
def test_retrieve_token(db):
    test_user = User.objects.create_user(username='test',
                             email='test@trakity.com',
                             password='password')
    test_user.save()

    # todo: how to set content_type='application/json' in the API client
    # Note: need to specify return Accept header or I'll get back JSON-API response
    # todo: how to specify a default Renderer per Application (though this need might go away if I extract this to a separate app)
    client = APIClient(HTTP_ACCEPT='application/json')

    # Test invalid user gets no token
    # Note: because not using the default content_type, need to explicitly set the data to a string and not expect it to
    # json.dumps() as it normally would (and should)
    result = client.post('/auth/token', '{"email": "test@trakity.com", "password": "not_password"}', content_type="application/json")
    assert(result.status_code == 401)

    result = client.post("/auth/token", '{"email": "test@trakity.com", "password": "password"}', content_type="application/json")
    assert(result.status_code == 200)
    tokens = result.json()
    assert('refresh' in tokens)
    assert('access' in tokens)


@pytest.mark.django_db
def test_blacklisting(db):
    """
    This test ensures that a used refresh token is blacklisted and can't be used again
    """
    user = User.objects.create_user(username='test', password='password', email='test@trakity.com')
    user.save()
    refresh_token = RefreshToken.for_user(user)

    assert(BlacklistedToken.objects.all().count() == 0)

    client = APIClient(HTTP_ACCEPT='application/json')
    result = client.post("/auth/token/refresh", '{"refresh": "' + str(refresh_token) + '"}',
                         content_type="application/json")
    assert(result.status_code == 200)

    result = client.post("/auth/token/refresh", '{"refresh": "' + str(refresh_token) + '"}',
                         content_type="application/json")
    assert (result.status_code == 401)
    assert (BlacklistedToken.objects.all().count() == 1)


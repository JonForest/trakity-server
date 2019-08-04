import pytest
from trakity_main.models import Task
from rest_framework.test import APIClient
# Will need to remove User model specific if we pull the Token work out into a separate App
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def _get_authorised_client():
    user = User.objects.create_user(username='test', password='password', email='test@trakity.com')
    user.save()
    token = RefreshToken.for_user(user)
    return APIClient(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')


def test_ping_pong(client):
    response = client.get('/status/ping')
    assert response.status_code == 200
    assert response.content == b'ping'


@pytest.mark.django_db
def test_get_task(db):
    client = _get_authorised_client()

    task = Task(description='This is a test task')
    task.save()

    assert(Task.objects.all().count() == 1)
    response = client.get('/tasks')
    assert(response.status_code == 200)
    assert(len(response.data) == 1)


@pytest.mark.django_db
def test_post_task(db):
    # todo: Get the client to log in
    client = _get_authorised_client()
    description = 'This is a test'

    new_task = {
        'data': {
            'type': 'tasks',
            'attributes': {
                'description': description,
                'start_date': '2020-01-01 13:00:12'
            }
        }
    }

    assert(Task.objects.all().count() == 0)
    response = client.post('/tasks', new_task)
    assert(response.status_code == 201)
    assert(Task.objects.all().count() == 1)
    assert(response.json()['data']['attributes']['description'] == description)


@pytest.mark.django_db
def test_update_task(db):
    client = _get_authorised_client()

    task = Task(description='This is a test task')
    task.save()

    description = 'This is an updated task'

    updated_task = {
        'data': {
            'id': task.id,
            'type': 'tasks',
            'attributes': {
                'description': description,
                'start_date': '2020-01-01 13:00:12'
            }
        }
    }

    response = client.patch(f'/tasks/{task.id}', updated_task)
    assert(response.status_code == 200)
    assert(response.json()['data']['attributes']['description'] == description)
    task = Task.objects.get(id=task.id)
    assert(task.description == description)



# @pytest.mark.django_db
# def test_delete_task(db):
#     """"
#     This will not be implemented for some time, most likely
#     """
#     pass

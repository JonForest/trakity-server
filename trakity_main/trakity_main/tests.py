import pytest
from trakity_main.models import Task


def test_ping_pong(client):
    response = client.get('/status/ping')
    assert response.status_code == 200
    assert response.content == b'ping'


@pytest.mark.django_db
def test_get_task(client):
    pass


@pytest.mark.django_db
def test_post_task(client):
    # todo: Get the client to log in
    new_task = {
        'data': {
            'type': 'tasks',
            'attributes': {
                'description': 'This is a test',
                'start_date': '2020-01-01 13:00:12'
            }
        }
    }

    assert (Task.objects.all().count() == 0)
    response = client.post('/tasks', new_task)
    assert(response.status_code == 201)
    assert(Task.objects.all().count() == 1)


@pytest.mark.django_db
def test_update_task(client):
    pass


@pytest.mark.django_db
def test_delete_task(client):
    """"
    This will not be implemented for some time, most likely
    """
    pass

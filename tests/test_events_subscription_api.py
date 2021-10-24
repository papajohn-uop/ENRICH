# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.event_subscription import EventSubscription  # noqa: F401
from openapi_server.models.event_subscription_input import EventSubscriptionInput  # noqa: F401


def test_register_listener(client: TestClient):
    """Test case for register_listener

    Register a listener
    """
    data = openapi_server.EventSubscriptionInput()

    headers = {
    }
    response = client.request(
        "POST",
        "/hub",
        headers=headers,
        json=data,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_unregister_listener(client: TestClient):
    """Test case for unregister_listener

    Unregister a listener
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/hub/{id}".format(id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


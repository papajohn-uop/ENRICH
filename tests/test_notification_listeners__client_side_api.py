# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.event_subscription import EventSubscription  # noqa: F401
from openapi_server.models.service_attribute_value_change_event import ServiceAttributeValueChangeEvent  # noqa: F401
from openapi_server.models.service_create_event import ServiceCreateEvent  # noqa: F401
from openapi_server.models.service_delete_event import ServiceDeleteEvent  # noqa: F401
from openapi_server.models.service_state_change_event import ServiceStateChangeEvent  # noqa: F401


def test_listen_to_service_attribute_value_change_event(client: TestClient):
    """Test case for listen_to_service_attribute_value_change_event

    Client listener for entity ServiceAttributeValueChangeEvent
    """
    data = openapi_server.ServiceAttributeValueChangeEvent()

    headers = {
    }
    response = client.request(
        "POST",
        "/listener/serviceAttributeValueChangeEvent",
        headers=headers,
        json=data,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_listen_to_service_create_event(client: TestClient):
    """Test case for listen_to_service_create_event

    Client listener for entity ServiceCreateEvent
    """
    data = openapi_server.ServiceCreateEvent()

    headers = {
    }
    response = client.request(
        "POST",
        "/listener/serviceCreateEvent",
        headers=headers,
        json=data,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_listen_to_service_delete_event(client: TestClient):
    """Test case for listen_to_service_delete_event

    Client listener for entity ServiceDeleteEvent
    """
    data = openapi_server.ServiceDeleteEvent()

    headers = {
    }
    response = client.request(
        "POST",
        "/listener/serviceDeleteEvent",
        headers=headers,
        json=data,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_listen_to_service_state_change_event(client: TestClient):
    """Test case for listen_to_service_state_change_event

    Client listener for entity ServiceStateChangeEvent
    """
    data = openapi_server.ServiceStateChangeEvent()

    headers = {
    }
    response = client.request(
        "POST",
        "/listener/serviceStateChangeEvent",
        headers=headers,
        json=data,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


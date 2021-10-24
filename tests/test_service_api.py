# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.service import Service  # noqa: F401
from openapi_server.models.service_create import ServiceCreate  # noqa: F401
from openapi_server.models.service_update import ServiceUpdate  # noqa: F401


def test_create_service(client: TestClient):
    """Test case for create_service

    Creates a Service
    """
    service = openapi_server.ServiceCreate()

    headers = {
    }
    response = client.request(
        "POST",
        "/service",
        headers=headers,
        json=service,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_service(client: TestClient):
    """Test case for delete_service

    Deletes a Service
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/service/{id}".format(id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_service(client: TestClient):
    """Test case for list_service

    List or find Service objects
    """
    params = [("fields", 'fields_example'),     ("offset", 56),     ("limit", 56)]
    headers = {
    }
    response = client.request(
        "GET",
        "/service",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_patch_service(client: TestClient):
    """Test case for patch_service

    Updates partially a Service
    """
    service = openapi_server.ServiceUpdate()

    headers = {
    }
    response = client.request(
        "PATCH",
        "/service/{id}".format(id='id_example'),
        headers=headers,
        json=service,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_retrieve_service(client: TestClient):
    """Test case for retrieve_service

    Retrieves a Service by ID
    """
    params = [("fields", 'fields_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/service/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


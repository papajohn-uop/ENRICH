# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error import Error
from openapi_server.models.event_subscription import EventSubscription
from openapi_server.models.service_attribute_value_change_event import ServiceAttributeValueChangeEvent
from openapi_server.models.service_create_event import ServiceCreateEvent
from openapi_server.models.service_delete_event import ServiceDeleteEvent
from openapi_server.models.service_state_change_event import ServiceStateChangeEvent


router = APIRouter()


@router.post(
    "/listener/serviceAttributeValueChangeEvent",
    responses={
        201: {"model": EventSubscription, "description": "Notified"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["notification listeners (client side)"],
    summary="Client listener for entity ServiceAttributeValueChangeEvent",
)
async def listen_to_service_attribute_value_change_event(
    data: ServiceAttributeValueChangeEvent = Body(None, description="The event data"),
) -> EventSubscription:
    """Example of a client listener for receiving the notification ServiceAttributeValueChangeEvent"""
    ...


@router.post(
    "/listener/serviceCreateEvent",
    responses={
        201: {"model": EventSubscription, "description": "Notified"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["notification listeners (client side)"],
    summary="Client listener for entity ServiceCreateEvent",
)
async def listen_to_service_create_event(
    data: ServiceCreateEvent = Body(None, description="The event data"),
) -> EventSubscription:
    """Example of a client listener for receiving the notification ServiceCreateEvent"""
    ...


@router.post(
    "/listener/serviceDeleteEvent",
    responses={
        201: {"model": EventSubscription, "description": "Notified"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["notification listeners (client side)"],
    summary="Client listener for entity ServiceDeleteEvent",
)
async def listen_to_service_delete_event(
    data: ServiceDeleteEvent = Body(None, description="The event data"),
) -> EventSubscription:
    """Example of a client listener for receiving the notification ServiceDeleteEvent"""
    ...


@router.post(
    "/listener/serviceStateChangeEvent",
    responses={
        201: {"model": EventSubscription, "description": "Notified"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["notification listeners (client side)"],
    summary="Client listener for entity ServiceStateChangeEvent",
)
async def listen_to_service_state_change_event(
    data: ServiceStateChangeEvent = Body(None, description="The event data"),
) -> EventSubscription:
    """Example of a client listener for receiving the notification ServiceStateChangeEvent"""
    ...

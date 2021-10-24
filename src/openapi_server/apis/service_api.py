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
from openapi_server.models.service import Service
from openapi_server.models.service_create import ServiceCreate
from openapi_server.models.service_update import ServiceUpdate


router = APIRouter()


@router.post(
    "/service",
    responses={
        201: {"model": Service, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["service"],
    summary="Creates a Service",
)
async def create_service(
    service: ServiceCreate = Body(None, description="The Service to be created"),
) -> Service:
    """This operation creates a Service entity."""
    ...


@router.delete(
    "/service/{id}",
    responses={
        204: {"description": "Deleted"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["service"],
    summary="Deletes a Service",
)
async def delete_service(
    id: str = Path(None, description="Identifier of the Service"),
) -> None:
    """This operation deletes a Service entity."""
    ...


@router.get(
    "/service",
    responses={
        200: {"model": List[Service], "description": "Success"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["service"],
    summary="List or find Service objects",
)
async def list_service(
    fields: str = Query(None, description="Comma-separated properties to be provided in response"),
    offset: int = Query(None, description="Requested index for start of resources to be provided in response"),
    limit: int = Query(None, description="Requested number of resources to be provided in response"),
) -> List[Service]:
    """This operation list or find Service entities"""
    ...


@router.patch(
    "/service/{id}",
    responses={
        200: {"model": Service, "description": "Updated"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["service"],
    summary="Updates partially a Service",
)
async def patch_service(
    id: str = Path(None, description="Identifier of the Service"),
    service: ServiceUpdate = Body(None, description="The Service to be updated"),
) -> Service:
    """This operation updates partially a Service entity."""
    ...


@router.get(
    "/service/{id}",
    responses={
        200: {"model": Service, "description": "Success"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["service"],
    summary="Retrieves a Service by ID",
)
async def retrieve_service(
    id: str = Path(None, description="Identifier of the Service"),
    fields: str = Query(None, description="Comma-separated properties to provide in response"),
) -> Service:
    """This operation retrieves a Service entity. Attribute selection is enabled for all first level attributes."""
    ...

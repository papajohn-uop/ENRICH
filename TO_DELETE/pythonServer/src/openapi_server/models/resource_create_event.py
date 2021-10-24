# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.resource_create_event_payload import ResourceCreateEventPayload


class ResourceCreateEvent(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResourceCreateEvent - a model defined in OpenAPI

        event: The event of this ResourceCreateEvent [Optional].
        event_id: The event_id of this ResourceCreateEvent [Optional].
        event_time: The event_time of this ResourceCreateEvent [Optional].
        event_type: The event_type of this ResourceCreateEvent [Optional].
        correlation_id: The correlation_id of this ResourceCreateEvent [Optional].
        domain: The domain of this ResourceCreateEvent [Optional].
        title: The title of this ResourceCreateEvent [Optional].
        description: The description of this ResourceCreateEvent [Optional].
        priority: The priority of this ResourceCreateEvent [Optional].
        time_ocurred: The time_ocurred of this ResourceCreateEvent [Optional].
    """

    event: Optional[ResourceCreateEventPayload] = None
    event_id: Optional[str] = None
    event_time: Optional[datetime] = None
    event_type: Optional[str] = None
    correlation_id: Optional[str] = None
    domain: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    time_ocurred: Optional[datetime] = None

ResourceCreateEvent.update_forward_refs()

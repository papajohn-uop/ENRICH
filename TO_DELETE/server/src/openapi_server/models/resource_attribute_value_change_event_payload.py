# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.resource import Resource


class ResourceAttributeValueChangeEventPayload(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResourceAttributeValueChangeEventPayload - a model defined in OpenAPI

        resource: The resource of this ResourceAttributeValueChangeEventPayload [Optional].
    """

    resource: Optional[Resource] = None

ResourceAttributeValueChangeEventPayload.update_forward_refs()
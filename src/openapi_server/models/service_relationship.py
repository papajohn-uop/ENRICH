# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.characteristic import Characteristic


class ServiceRelationship(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceRelationship - a model defined in OpenAPI

        relationship_type: The relationship_type of this ServiceRelationship.
        service: The service of this ServiceRelationship.
        service_relationship_characteristic: The service_relationship_characteristic of this ServiceRelationship [Optional].
    """

    relationship_type: str
    service: ServiceRefOrValue
    service_relationship_characteristic: Optional[List[Characteristic]] = None


from openapi_server.models.service_ref_or_value import ServiceRefOrValue

ServiceRelationship.update_forward_refs()

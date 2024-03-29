# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.characteristic_relationship import CharacteristicRelationship


class Characteristic(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Characteristic - a model defined in OpenAPI

        id: The id of this Characteristic [Optional].
        name: The name of this Characteristic.
        value_type: The value_type of this Characteristic [Optional].
        characteristic_relationship: The characteristic_relationship of this Characteristic [Optional].
        value: The value of this Characteristic.
        base_type: The base_type of this Characteristic [Optional].
        schema_location: The schema_location of this Characteristic [Optional].
        type: The type of this Characteristic [Optional].
    """

    id: Optional[str] = None
    name: str
    value_type: Optional[str] = None
    characteristic_relationship: Optional[List[CharacteristicRelationship]] = None
    value: Dict[str, Any]
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = None

Characteristic.update_forward_refs()

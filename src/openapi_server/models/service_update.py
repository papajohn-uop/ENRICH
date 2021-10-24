# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.characteristic import Characteristic
from openapi_server.models.feature import Feature
from openapi_server.models.note import Note
from openapi_server.models.related_entity_ref_or_value import RelatedEntityRefOrValue
from openapi_server.models.related_party import RelatedParty
from openapi_server.models.related_place_ref_or_value import RelatedPlaceRefOrValue
from openapi_server.models.related_service_order_item import RelatedServiceOrderItem
from openapi_server.models.resource_ref import ResourceRef
from openapi_server.models.service_ref_or_value import ServiceRefOrValue
from openapi_server.models.service_relationship import ServiceRelationship
from openapi_server.models.service_specification_ref import ServiceSpecificationRef
from openapi_server.models.service_state_type import ServiceStateType


class ServiceUpdate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceUpdate - a model defined in OpenAPI

        category: The category of this ServiceUpdate [Optional].
        description: The description of this ServiceUpdate [Optional].
        end_date: The end_date of this ServiceUpdate [Optional].
        has_started: The has_started of this ServiceUpdate [Optional].
        is_bundle: The is_bundle of this ServiceUpdate [Optional].
        is_service_enabled: The is_service_enabled of this ServiceUpdate [Optional].
        is_stateful: The is_stateful of this ServiceUpdate [Optional].
        name: The name of this ServiceUpdate [Optional].
        service_type: The service_type of this ServiceUpdate [Optional].
        start_date: The start_date of this ServiceUpdate [Optional].
        start_mode: The start_mode of this ServiceUpdate [Optional].
        feature: The feature of this ServiceUpdate [Optional].
        note: The note of this ServiceUpdate [Optional].
        place: The place of this ServiceUpdate [Optional].
        related_entity: The related_entity of this ServiceUpdate [Optional].
        related_party: The related_party of this ServiceUpdate [Optional].
        service_characteristic: The service_characteristic of this ServiceUpdate [Optional].
        service_order_item: The service_order_item of this ServiceUpdate [Optional].
        service_relationship: The service_relationship of this ServiceUpdate [Optional].
        service_specification: The service_specification of this ServiceUpdate [Optional].
        state: The state of this ServiceUpdate [Optional].
        supporting_resource: The supporting_resource of this ServiceUpdate [Optional].
        supporting_service: The supporting_service of this ServiceUpdate [Optional].
    """

    category: Optional[str] = None
    description: Optional[str] = None
    end_date: Optional[datetime] = None
    has_started: Optional[bool] = None
    is_bundle: Optional[bool] = None
    is_service_enabled: Optional[bool] = None
    is_stateful: Optional[bool] = None
    name: Optional[str] = None
    service_type: Optional[str] = None
    start_date: Optional[datetime] = None
    start_mode: Optional[str] = None
    feature: Optional[List[Feature]] = None
    note: Optional[List[Note]] = None
    place: Optional[List[RelatedPlaceRefOrValue]] = None
    related_entity: Optional[List[RelatedEntityRefOrValue]] = None
    related_party: Optional[List[RelatedParty]] = None
    service_characteristic: Optional[List[Characteristic]] = None
    service_order_item: Optional[List[RelatedServiceOrderItem]] = None
    service_relationship: Optional[List[ServiceRelationship]] = None
    service_specification: Optional[ServiceSpecificationRef] = None
    state: Optional[ServiceStateType] = None
    supporting_resource: Optional[List[ResourceRef]] = None
    supporting_service: Optional[List[ServiceRefOrValue]] = None

ServiceUpdate.update_forward_refs()

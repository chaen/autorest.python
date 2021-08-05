# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._pets_operations import (
    build_create_ap_in_properties_request,
    build_create_ap_in_properties_with_ap_string_request,
    build_create_ap_object_request,
    build_create_ap_string_request,
    build_create_ap_true_request,
    build_create_cat_ap_true_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetsOperations:
    """PetsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create_ap_true(self, create_parameters: Any, **kwargs: Any) -> Any:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "": {
                        "str": "any (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "": {
                        "str": "any (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = create_parameters

        request = build_create_ap_true_request(
            content_type=content_type,
            json=json,
            template_url=self.create_ap_true.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_true.metadata = {"url": "/additionalProperties/true"}  # type: ignore

    @distributed_trace_async
    async def create_cat_ap_true(self, create_parameters: Any, **kwargs: Any) -> Any:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "friendly": "bool (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "friendly": "bool (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = create_parameters

        request = build_create_cat_ap_true_request(
            content_type=content_type,
            json=json,
            template_url=self.create_cat_ap_true.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_cat_ap_true.metadata = {"url": "/additionalProperties/true-subclass"}  # type: ignore

    @distributed_trace_async
    async def create_ap_object(self, create_parameters: Any, **kwargs: Any) -> Any:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "": {
                        "str": "any (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "": {
                        "str": "any (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = create_parameters

        request = build_create_ap_object_request(
            content_type=content_type,
            json=json,
            template_url=self.create_ap_object.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_object.metadata = {"url": "/additionalProperties/type/object"}  # type: ignore

    @distributed_trace_async
    async def create_ap_string(self, create_parameters: Any, **kwargs: Any) -> Any:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "": {
                        "str": "str (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "": {
                        "str": "str (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = create_parameters

        request = build_create_ap_string_request(
            content_type=content_type,
            json=json,
            template_url=self.create_ap_string.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_string.metadata = {"url": "/additionalProperties/type/string"}  # type: ignore

    @distributed_trace_async
    async def create_ap_in_properties(self, create_parameters: Any, **kwargs: Any) -> Any:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "additionalProperties": {
                        "str": "float (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "additionalProperties": {
                        "str": "float (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = create_parameters

        request = build_create_ap_in_properties_request(
            content_type=content_type,
            json=json,
            template_url=self.create_ap_in_properties.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_in_properties.metadata = {"url": "/additionalProperties/in/properties"}  # type: ignore

    @distributed_trace_async
    async def create_ap_in_properties_with_ap_string(self, create_parameters: Any, **kwargs: Any) -> Any:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "": {
                        "str": "str (optional)"
                    },
                    "@odata.location": "str",
                    "additionalProperties": {
                        "str": "float (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "": {
                        "str": "str (optional)"
                    },
                    "@odata.location": "str",
                    "additionalProperties": {
                        "str": "float (optional)"
                    },
                    "id": "int",
                    "name": "str (optional)",
                    "status": "bool (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = create_parameters

        request = build_create_ap_in_properties_with_ap_string_request(
            content_type=content_type,
            json=json,
            template_url=self.create_ap_in_properties_with_ap_string.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_in_properties_with_ap_string.metadata = {"url": "/additionalProperties/in/properties/with/additionalProperties/string"}  # type: ignore

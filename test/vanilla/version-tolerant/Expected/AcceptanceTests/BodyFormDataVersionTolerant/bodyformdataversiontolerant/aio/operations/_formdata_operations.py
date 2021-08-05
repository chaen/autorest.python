# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar
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

from ...operations._formdata_operations import (
    build_upload_file_request,
    build_upload_file_via_body_request,
    build_upload_files_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class FormdataOperations:
    """FormdataOperations async operations.

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
    async def upload_file(self, files: Dict[str, Any], **kwargs: Any) -> IO:
        """Upload file.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: IO
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", None)  # type: Optional[str]

        files = None
        data = None
        # Construct form data
        files = {
            "fileContent": file_content,
            "fileName": file_name,
        }

        request = build_upload_file_request(
            content_type=content_type,
            files=files,
            data=data,
            template_url=self.upload_file.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=True, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_file.metadata = {"url": "/formdata/stream/uploadfile"}  # type: ignore

    @distributed_trace_async
    async def upload_file_via_body(self, file_content: IO, **kwargs: Any) -> IO:
        """Upload file.

        :param file_content: File to upload.
        :type file_content: IO
        :return: IO
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/octet-stream")  # type: Optional[str]

        content = file_content

        request = build_upload_file_via_body_request(
            content_type=content_type,
            content=content,
            template_url=self.upload_file_via_body.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=True, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_file_via_body.metadata = {"url": "/formdata/stream/uploadfile"}  # type: ignore

    @distributed_trace_async
    async def upload_files(self, files: Dict[str, Any], **kwargs: Any) -> IO:
        """Upload multiple files.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: IO
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # multipart input template you can fill out and use as your `files` input.
                files = {
                    "file_content": [
                        "IO. Files to upload."
                    ]
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", None)  # type: Optional[str]

        files = None
        data = None
        # Construct form data
        files = {
            "fileContent": file_content,
        }

        request = build_upload_files_request(
            content_type=content_type,
            files=files,
            data=data,
            template_url=self.upload_files.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=True, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_files.metadata = {"url": "/formdata/stream/uploadfiles"}  # type: ignore

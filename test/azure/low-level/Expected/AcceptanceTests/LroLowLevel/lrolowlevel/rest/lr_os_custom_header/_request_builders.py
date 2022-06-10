# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, IO, Optional, Union, overload

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

@overload
def build_put_async_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running put request, service returns a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", and "OK".
                },
                "tags": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """


@overload
def build_put_async_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running put request, service returns a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put_async_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running put request, service returns a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/customheader/putasync/retry/succeeded"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_put201_creating_succeeded200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running put request, service returns a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", and "OK".
                },
                "tags": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """


@overload
def build_put201_creating_succeeded200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running put request, service returns a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put201_creating_succeeded200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running put request, service returns a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/customheader/put/201/creating/succeeded/200"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_post202_retry200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running post request, service returns a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", and "OK".
                },
                "tags": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """


@overload
def build_post202_retry200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running post request, service returns a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_post202_retry200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running post request, service returns a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/customheader/post/202/retry/200"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_post_async_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running post request, service returns a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", and "OK".
                },
                "tags": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """


@overload
def build_post_async_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running post request, service returns a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_post_async_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running post request, service returns a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/customheader/postasync/retry/succeeded"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )

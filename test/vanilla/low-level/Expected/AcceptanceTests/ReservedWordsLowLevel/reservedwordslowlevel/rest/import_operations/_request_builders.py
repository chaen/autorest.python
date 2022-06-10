# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._serialization import Serializer

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_operation_one_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Operation in operation group import, a reserved word.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword parameter1: Pass in 'foo' to pass this test. Required.
    :paramtype parameter1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    parameter1 = kwargs.pop('parameter1')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reservedWords/operationGroup/import"

    # Construct parameters
    _params['parameter1'] = _SERIALIZER.query("parameter1", parameter1, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

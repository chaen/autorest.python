# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import AutoRestPagingTestServiceConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class AutoRestPagingTestService:
    """Long-running Operation for AutoRest.

    :keyword endpoint: Service URL. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(self, *, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:

        self._config = AutoRestPagingTestServiceConfiguration(**kwargs)
        self._client = PipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `paginglowlevel.rest`.
        Use these helper methods to create the request you pass to this method.

        >>> from paginglowlevel.rest import paging
        >>> request = paging.build_get_no_item_name_pages_request(**kwargs)
        <HttpRequest [GET], url: '/paging/noitemname'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestPagingTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)

# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from ._configuration import AutoRestParameterizedCustomHostTestClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class AutoRestParameterizedCustomHostTestClient:
    """Test Infrastructure for AutoRest.

    :param subscription_id: The subscription id with value 'test12'.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the parameterized host.
     Default value 'host'. Default value is "host".
    :type dns_suffix: str
    """

    def __init__(self, subscription_id: str, dns_suffix: str = "host", **kwargs: Any) -> None:
        _endpoint = "{vault}{secret}{dnsSuffix}"
        self._config = AutoRestParameterizedCustomHostTestClientConfiguration(
            subscription_id=subscription_id, dns_suffix=dns_suffix, **kwargs
        )
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `custombaseurlmoreoptionslowlevel.rest`.
        Use these helper methods to create the request you pass to this method.

        >>> from custombaseurlmoreoptionslowlevel.rest import paths
        >>> request = paths.build_get_empty_request(key_name, subscription_id, key_version=key_version, **kwargs)
        <HttpRequest [GET], url: '/customuri/{subscriptionId}/{keyName}'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "dnsSuffix": self._serialize.url(
                "self._config.dns_suffix", self._config.dns_suffix, "str", skip_quote=True
            ),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestParameterizedCustomHostTestClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)

# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import ResiliencyServiceDrivenClientConfiguration
from ._operations import ResiliencyServiceDrivenClientOperationsMixin
from ._serialization import Deserializer, Serializer


class ResiliencyServiceDrivenClient(
    ResiliencyServiceDrivenClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword
    """Test that we can grow up a service spec and service deployment into a multi-versioned service
    with full client support.

    :param endpoint: Need to be set as 'http://localhost:3000' in client. Required.
    :type endpoint: str
    :param service_deployment_version: Pass in either 'v1' or 'v2'. This represents a version of
     the service deployment in history. 'v1' is for the deployment when the service had only one api
     version. 'v2' is for the deployment when the service had api-versions 'v1' and 'v2'. Required.
    :type service_deployment_version: str
    :keyword api_version: Pass in 'v1'. This represents the API version of the service. Will grow
     up in the next deployment to be both 'v1' and 'v2'. Default value is "v1". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, service_deployment_version: str, **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}/resiliency/service-driven/client:v1/service:{serviceDeploymentVersion}/api-version:{apiVersion}"  # pylint: disable=line-too-long
        self._config = ResiliencyServiceDrivenClientConfiguration(
            endpoint=endpoint, service_deployment_version=service_deployment_version, **kwargs
        )
        self._client: PipelineClient = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ResiliencyServiceDrivenClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)

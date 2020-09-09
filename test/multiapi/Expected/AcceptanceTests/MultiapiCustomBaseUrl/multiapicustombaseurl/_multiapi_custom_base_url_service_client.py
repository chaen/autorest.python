# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import MultiapiCustomBaseUrlServiceClientConfiguration
from ._operations_mixin import MultiapiCustomBaseUrlServiceClientOperationsMixin
class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class MultiapiCustomBaseUrlServiceClient(MultiapiCustomBaseUrlServiceClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """Service client for multiapi custom base url testing.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param endpoint: Pass in https://localhost:3000.
    :type endpoint: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2.0.0'
    _PROFILE_TAG = "multiapicustombaseurl.MultiapiCustomBaseUrlServiceClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        endpoint,  # type: str
        api_version=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ):
        if api_version == '1.0.0':
            base_url = '{Endpoint}/multiapiCustomBaseUrl/v1'
        elif api_version == '2.0.0':
            base_url = '{Endpoint}/multiapiCustomBaseUrl/v2'
        else:
            raise NotImplementedError("API version {} is not available".format(api_version))
        self._config = MultiapiCustomBaseUrlServiceClientConfiguration(credential, endpoint, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(MultiapiCustomBaseUrlServiceClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 1.0.0: :mod:`v1.models<multiapicustombaseurl.v1.models>`
           * 2.0.0: :mod:`v2.models<multiapicustombaseurl.v2.models>`
        """
        if api_version == '1.0.0':
            from .v1 import models
            return models
        elif api_version == '2.0.0':
            from .v2 import models
            return models
        raise NotImplementedError("API version {} is not available".format(api_version))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)

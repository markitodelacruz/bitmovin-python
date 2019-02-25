# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.mp3_muxing import Mp3Muxing
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.muxings.mp3.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.mp3.information.information_api import InformationApi
from bitmovin_python.encoding.encodings.muxings.mp3.mp3_muxings_list_query_params import Mp3MuxingsListQueryParams


class Mp3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(Mp3Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.information = InformationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, encoding_id, mp3_muxing=None, **kwargs):
        """Add MP3 Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/mp3',
            mp3_muxing,
            path_params={'encoding_id': encoding_id},
            type=Mp3Muxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete MP3 Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/mp3/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """MP3 Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp3/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=Mp3Muxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: Mp3MuxingsListQueryParams = None, **kwargs):
        """List MP3 Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp3',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Mp3Muxing,
            **kwargs
        )
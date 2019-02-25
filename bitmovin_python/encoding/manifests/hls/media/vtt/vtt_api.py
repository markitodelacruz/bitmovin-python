# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.vtt_media_info import VttMediaInfo
from bitmovin_python.encoding.manifests.hls.media.vtt.vtt_media_infos_list_query_params import VttMediaInfosListQueryParams


class VttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(VttApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, manifest_id, vtt_media_info=None, **kwargs):
        """Add VTT Media"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/vtt',
            vtt_media_info,
            path_params={'manifest_id': manifest_id},
            type=VttMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        """Delete VTT Media"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/vtt/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        """VTT Media Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/vtt/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=VttMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params: VttMediaInfosListQueryParams = None, **kwargs):
        """List all VTT Media"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/vtt',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=VttMediaInfo,
            **kwargs
        )
# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.drm import Drm
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.muxings.mp4.drm.playready.playready_api import PlayreadyApi
from bitmovin_python.encoding.encodings.muxings.mp4.drm.clearkey.clearkey_api import ClearkeyApi
from bitmovin_python.encoding.encodings.muxings.mp4.drm.widevine.widevine_api import WidevineApi
from bitmovin_python.encoding.encodings.muxings.mp4.drm.marlin.marlin_api import MarlinApi
from bitmovin_python.encoding.encodings.muxings.mp4.drm.cenc.cenc_api import CencApi


class DrmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(DrmApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.playready = PlayreadyApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.clearkey = ClearkeyApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.widevine = WidevineApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.marlin = MarlinApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.cenc = CencApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, **kwargs):
        """List all DRM configurations of MP4 Muxing"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            pagination_response=True,
            type=Drm,
            **kwargs
        )
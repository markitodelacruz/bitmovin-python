# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.custom_player_build_download import CustomPlayerBuildDownload
from bitmovin_python.models.response_envelope import ResponseEnvelope


class DownloadApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(DownloadApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, custom_build_id, **kwargs):
        """Custom Web Player Build Download Link"""

        return self.api_client.get(
            '/player/custom-builds/web/{custom_build_id}/download',
            path_params={'custom_build_id': custom_build_id},
            type=CustomPlayerBuildDownload,
            **kwargs
        )
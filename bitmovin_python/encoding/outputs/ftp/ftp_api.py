# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.ftp_output import FtpOutput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.outputs.ftp.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.outputs.ftp.ftp_outputs_list_query_params import FtpOutputsListQueryParams


class FtpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(FtpApi, self).__init__(
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

    def create(self, ftp_output=None, **kwargs):
        """Create FTP Output"""

        return self.api_client.post(
            '/encoding/outputs/ftp',
            ftp_output,
            type=FtpOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete FTP Output"""

        return self.api_client.delete(
            '/encoding/outputs/ftp/{output_id}',
            path_params={'output_id': output_id},
            type=FtpOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """FTP Output Details"""

        return self.api_client.get(
            '/encoding/outputs/ftp/{output_id}',
            path_params={'output_id': output_id},
            type=FtpOutput,
            **kwargs
        )

    def list(self, query_params: FtpOutputsListQueryParams = None, **kwargs):
        """List FTP Outputs"""

        return self.api_client.get(
            '/encoding/outputs/ftp',
            query_params=query_params,
            pagination_response=True,
            type=FtpOutput,
            **kwargs
        )
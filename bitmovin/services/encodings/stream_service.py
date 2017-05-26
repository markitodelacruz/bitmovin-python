from bitmovin.errors import BitmovinApiError, MissingArgumentError, InvalidStatusError
from bitmovin.resources import Status, ResourceResponse
from bitmovin.resources.models import Stream as StreamResource, EncodingStatus
from ..rest_service import RestService
from .sprite_service import SpriteService


class Stream(RestService):
    BASE_ENDPOINT_URL = 'encoding/encodings/{encoding_id}/streams'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=StreamResource)
        self.Sprite = SpriteService(http_client=http_client)

    def _get_endpoint_url(self, encoding_id):
        if not encoding_id:
            raise MissingArgumentError('encoding_id must be given')
        return self.BASE_ENDPOINT_URL.replace('{encoding_id}', encoding_id)

    def create(self, object_, encoding_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().create(object_)

    def delete(self, encoding_id, stream_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().delete(id_=stream_id)

    def retrieve(self, encoding_id, stream_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().retrieve(id_=stream_id)

    def list(self, encoding_id, offset=None, limit=None):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().list(offset, limit)

    def retrieve_custom_data(self, encoding_id, stream_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().retrieve_custom_data(id_=stream_id)

from app.api.common.base import BaseResource


class SpotifyCallback(BaseResource):

    def on_get(self, req, res):
        print('bateu aqui ein')
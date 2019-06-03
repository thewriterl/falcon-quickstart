from app.api.common.base import BaseResource
from app.api.v2.spotifyAuth import SpotifyAuth
from app.api.model.welcome import Welcome
import requests
import json


class SpotifyTracks(BaseResource):

    def on_get(self, req, res):

        spotiAuth = SpotifyAuth()
        auth = spotiAuth.auth()

        header = {'Authorization': 'Bearer ' + auth['access_token']}

        tracks = requests.get('https://api.spotify.com/v1/me/tracks?limit=1', headers=header)

        ok = json.loads(tracks.content.decode('utf8'))

        tracks = Welcome(json=json)

        res.body = self.to_json(ok)

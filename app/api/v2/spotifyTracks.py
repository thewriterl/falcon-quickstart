from app.api.common.base import BaseResource
from app.api.v2.spotifyAuth import SpotifyAuth
import requests
import json


class SpotifyTracks(BaseResource):

    def on_get(self, req, res):

        spotiAuth = SpotifyAuth()
        auth = spotiAuth.auth()

        header = {'Authorization': 'Bearer ' + auth['access_token']}

        print('asdfff')


        tracks = requests.get('https://api.spotify.com/v1/me/tracks?limit=1', headers=header)

        ok = json.loads(tracks.content.decode('utf8'))

        res.body = self.to_json(ok)


        print('asdf')
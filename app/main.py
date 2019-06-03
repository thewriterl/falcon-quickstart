import falcon

from app import log
from app.middleware.auth import AuthHandler

from app.middleware.translator import JSONTranslator

from app.api.common import base
from app.api.v2 import spotifyCallback, spotifyAuth, spotifyTracks
from app.errors import AppError

LOG = log.get_logger()

class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        LOG.info('API Server is starting')

        self.add_route('/', base.BaseResource())
        self.add_route('/authorize', spotifyAuth.SpotifyAuth())
        self.add_route('/callback', spotifyCallback.SpotifyCallback())
        self.add_route('/tracks', spotifyTracks.SpotifyTracks())
        self.add_route('/callback', spotifyAuth.SpotifyCallback())

        self.add_error_handler(AppError, AppError.handle)

# init_session()
# middleware = [AuthHandler(), JSONTranslator(), DatabaseSessionManager(db_session)]
middleware = [AuthHandler(), JSONTranslator()]
application = App(middleware=middleware)

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()

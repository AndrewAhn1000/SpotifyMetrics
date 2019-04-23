from oauth2 import SpotifyOAuth, SpotifyOauthError, SpotifyClientCredentials
from bottle import route, run, request
import config 
import os
import webbrowser

scope_params = 'user-read-recently-played user-library-modify playlist-read-private user-read-email'
c = SpotifyOAuth(client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET, redirect_uri=config.REDIRECT_URI, scope=scope_params, cache_path=os.getcwd())

@route('/')
def device_session():
    auth_url = c.get_authorize_url()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton

@route('/callback', method='GET')
def get_auth_code():
    redirect_uri = request.url
    return '<p>'+redirect_uri+'</p>'

run(host='localhost', port=8080)



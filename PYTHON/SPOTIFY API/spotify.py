from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

class MySpotify:
    def __init__(self):
        self.CLIENT_ID = ""
        self.CLIENT_SECRET = ""
        self.REDIRECT_URI = "http://example.com"
        self.SCOPE="playlist-modify-public playlist-modify-private"
        self.USERNAME=""
    def _create_playlist(self,name_playlist):
        server=Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID,client_secret=self.CLIENT_SECRET,redirect_uri=self.REDIRECT_URI,scope=self.SCOPE,cache_path="token.txt",username=self.USERNAME,show_dialog=True))
        return server.user_playlist_create(user=self.USERNAME,name=name_playlist)

a=MySpotify()
result=a._create_playlist(name_playlist="hi1")
print(result)
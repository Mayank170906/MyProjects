from song import Song
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


USER=input("In which year you would like to travel to ? (YY-MM-DD)\nNote input should be greater than 2005")

data=Song()
top_100_songs=data._100songs(user=USER)
CLIENT_ID = "b864936c97c44741a5cb7ef57617aba7"
CLIENT_SECRET = "4745d1ab820a496e93b7f6dd8fbff905"
REDIRECT_URI = "http://example.com"
SCOPE="playlist-modify-public playlist-modify-private"
USERNAME="312dc5j25mgii5yb5y2wbvls5cwi"
PLAYLIST_URI="https://open.spotify.com/playlist/1UpBTaupjnaF9BZlMeJ9Vo?si=27eed191cad546d0"
server=Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope=SCOPE,cache_path="token.txt",username=USERNAME,show_dialog=True))
server.user_playlist_create(user=USERNAME,name=USER)
all_url=[]
for song in  top_100_songs:
    data_song=server.search(q=f"track:{song}")
    try:
        url=data_song['tracks']['items'][0]['external_urls']['spotify']
        print(url)
        server.playlist_add_items(playlist_id=PLAYLIST_URI,items=[url])
    except:
        print("Sorry not available on spotify.")


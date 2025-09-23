import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from time import sleep

#client id and client secret id
cid ="14c55845de774de096c848cfe3445d9f"
secret ="50ecc0a14e1e4108abee949dc7fd13df"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))

def find(artist):
    try:
        result = sp.search(q=artist, type="artist")
        art = result['artists']['items'][0]
        genre = art['genres']
        if not genre:
            return "NULL"
        sleep(0.5)
        return genre[0]
    except:
        return "stops working"


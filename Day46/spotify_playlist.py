# import requests
# from bs4 import BeautifulSoup
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

# INDIAN_BASE_URL = "https://www.billboard.com/charts/india-songs-hotw/"
# BASE_URL = "https://www.billboard.com/charts/hot-100/"

# # spotify URL
# SPOTIFY_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize?'
REIDRECT_URL = "https://open.spotify.com/"

CLIENT_ID= "f83d1e9639b64c20811589787ff9a592"
CLIENT_SECRET = "430a6f359cbb4f7081abfefbfef73312"


# krsna_uri = "spotify:artist:5C1S9XwxMuuCciutwMhp5t"



# session = requests.Session()
# session.verify = False

# # Patch the requests methods in spotipy to use this session
# # original_request = requests.Session.request

# # def patched_request(self, method, url, *args, **kwargs):
# #     kwargs['verify'] = False
# #     return original_request(self, method, url, *args, **kwargs)

# # requests.Session.request = patched_request

# # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= CLIENT_ID,
# #                                                client_secret= CLIENT_SECRET,
# #                                                redirect_uri= REIDRECT_URL,
# #                                                scope="user-library-read", 
# #                                                ))

# # results = sp.artist_albums(krsna_uri, album_type='album')
# # albums = results['items']
# # while results['next']:
# #     results = sp.next(results)
# #     albums.extend(results['items'])

# # for album in albums:
# #     print(album['name'])

# # date  = input("Which year's top 100 songs do you want, Enter in YYYY-MM-DD format: ")


# # response = requests.get(url= f"{BASE_URL}/{date}", verify= False)
# # response = requests.get(url= f"{INDIAN_BASE_URL}/{date}", verify= False)
# # contents = response.text

# # # print(contents)
# # soup = BeautifulSoup(contents, 'html.parser')

# # song_name = soup.select(selector= "li ul li h3")
# # songs = [songs.getText().strip() for songs in song_name]

# # print(songs)

# # Getting Authorization from spotify

# sp = spotipy.Spotify( auth_manager = SpotifyOAuth(
#     client_id = CLIENT_ID,
#     client_secret = CLIENT_SECRET,
#     redirect_uri = REIDRECT_URL,
#     scope = "playlist-modify-private",
#     show_dialog = True,
#     cache_path="token.txt",
#     username = "31m5risp2bzxwzig2frreqimivni"
# ))


# user_id = sp.current_user()["id"]

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date, verify= False)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri= REIDRECT_URL,
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

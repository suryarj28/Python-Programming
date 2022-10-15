import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? type the data in this format YYYY-MM-DD:")


# STEP 1

url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
songs_names_h3 = soup.select(".o-chart-results-list__item h3.c-title")
songs_names = [song.getText().strip() for song in songs_names_h3]
print(songs_names)

# STEP 2

Client_ID = "af1d4f5b29a84e088ca117dada7459d0"
Client_Secret = "dc2e3b682aee4bbd9d81e579fd13729e"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)


# STEP 3

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in songs_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

    except IndexError:
        print(f"{song} doesn't exisit in spotify skipped")


# STEP 4

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)


#Adding songs found into the new playlist

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

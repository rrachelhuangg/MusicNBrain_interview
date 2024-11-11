#show good documentation and clean code, examples

#very broad prompt: locate the most interesting 5 seconds from a song

#types of song input: audio files (from spotify, soundcloud), text files of the notes (assip), song title
#definition of interesting 5 seconds: main melody, loudest, fastest, most instruments used, variation on the melody

# idea 1: use librosa and spotipy to select fastest/loudest/highest energy... parts of songs using track ids

# idea 2: assip method: musescore plugin to convert sheet music to abc (export notes?) text file: and then do analysis with note patterns on that (and possibly try regex?)

# harmonic analysis/time series analysis?

import librosa
import spotipy
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "1b03b661f34d492eaabc7c330c4fe7b0"
client_secret = "db06c4a9312a46eda1bbf8a79aa8f53e"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def analyze_song(track_id):
    features = spotify.audio_features(track_id)
    tempo = features[0]['tempo'] if features else None
    key = features[0]['key'] if features else None

    return {"tempo": tempo, "key": key}

track_id = "2iUmqdfGZcHIhS3b9E9EWq"
sections = analyze_song(track_id)
print(sections)

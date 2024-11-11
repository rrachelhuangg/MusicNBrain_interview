#show good documentation and clean code, examples

#very broad prompt: locate the most interesting 5 seconds from a song

#types of song input: audio files (from spotify, soundcloud), text files of the notes (assip), song title
#definition of interesting 5 seconds: main melody, loudest, fastest, most instruments used, variation on the melody

# idea 1: use librosa and spotipy to select fastest/loudest/highest energy... parts of songs using track ids

# idea 2: assip method: musescore plugin to convert sheet music to abc (export notes?) text file: and then do analysis with note patterns on that (and possibly try regex?)

# harmonic analysis/time series analysis?
#visualize the song audio files
#cli

import librosa
import datetime
import sounddevice
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import click

def viz_songwaves(song_file_name):
    sound, sr = librosa.load(song_file_name, sr=None)

    fig, ax = plt.subplots()
    librosa.display.waveshow(sound, sr=sr, ax=ax)
    ax.set(title='Soundwave amplitude of song over time')
    plt.xlabel('Time(seconds)')
    plt.ylabel('Amplitude')
    fig.savefig('soundwave_amplitude_visualization.jpg')

    fig, ax = plt.subplots()
    hop_length = 2048
    D = librosa.amplitude_to_db(np.abs(librosa.stft(sound, hop_length=hop_length)), ref=np.max)
    img = librosa.display.specshow(D, y_axis='log', sr=sr, hop_length=hop_length, x_axis='time', ax=ax)
    ax.set(title='Log-frequency power spectrogram')
    ax.label_outer()
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    fig.savefig('soundwave_log-frequency_visualization.jpg')

def viz_songnotes(song_file_name):
    sound, sr = librosa.load(song_file_name, sr=None)

    chroma = librosa.feature.chroma_stft(y=sound)

    fig, ax = plt.subplots()
    img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
    ax.set(title="Chromagram demonstration (Frequency of notes in song over time)")
    fig.colorbar(img, ax=ax)
    fig.savefig('song_notes.jpg')

    ccov = np.cov(chroma)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(ccov, y_axis='chroma', x_axis='chroma', ax=ax)
    ax.set(title='Chroma covariance')
    fig.colorbar(img, ax=ax)
    fig.savefig('important_song_notes.jpg')

def general_song_analysis(song_file_name):
    sound, sr = librosa.load(song_file_name, sr=None)

    tempo, beats = librosa.beat.beat_track(y=sound, sr=sr)
    length = librosa.get_duration(y=sound, sr=sr)

    print("The tempo of the song is: " + str(round(tempo[0])) + " BPM")
    print("The song length is: " + str(datetime.timedelta(seconds=round(length))))

def analyze_instruments(song_file_name):
    sound, sr = librosa.load(song_file_name, sr=None)

    y_harmonic, y_percussive = librosa.effects.hpss(sound)

    fig, ax = plt.subplots()
    librosa.display.waveshow(y_harmonic, sr=sr, ax=ax)
    ax.set(title='Amplitude of the Harmonic Instrument Soundwaves Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    fig.savefig('harmonic_instrument_soundwaves.jpg')

    fig, ax = plt.subplots()
    librosa.display.waveshow(y_percussive, sr=sr, ax=ax)
    ax.set(title='Amplitude of the Percussive Instrument Soundwaves Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    fig.savefig('percussive_instrument_soundwaves.jpg')

def soundwave_analysis(song_file_name):
    file_name = song_file_name
    frame_length = 2048
    hop_length = 512
    num_seconds_of_slice = 5

    sound, sr = librosa.load(file_name, sr = None)

    clip_rms = librosa.feature.rms(y=sound, frame_length=frame_length, hop_length=hop_length)
    clip_rms = clip_rms.squeeze()

    peak_rms_index = clip_rms.argmax()
    peak_index = peak_rms_index*hop_length+int(frame_length/2)

    half_slice_width = int(num_seconds_of_slice*sr/2)
    left_index = max(0, peak_index-half_slice_width)
    right_index = peak_index+half_slice_width
    sound_slice = sound[left_index:right_index]

    sounddevice.play(sound_slice, sr)
    sounddevice.wait()

@click.group
def main():
    """Extract the most interesting 5 seconds from a song"""

@main.command()
@click.option(
    '--song-file-name',
    default='Halsey.mp3',
    type=str,
    help='Optional: Input file name of song to analyze.'
)
@click.option(
    '--type-of-analysis',
    default='s',
    type=str,
    help='Optional: Type of analysis desired. s is for soundwave analysis, t is for text analysis.'
)

def extract_five(
    song_file_name,
    type_of_analysis
):
    """Extract the most interesting 5 seconds from a song using desired type of analysis."""
    if type_of_analysis == 's':
        print("soundwave analysis")
        soundwave_analysis(song_file_name)
        viz_songwaves(song_file_name)
        viz_songnotes(song_file_name)
        general_song_analysis(song_file_name)
        analyze_instruments(song_file_name)
    elif type_of_analysis == 't':
        print("text analysis")

if __name__ == '__main__':
    main()

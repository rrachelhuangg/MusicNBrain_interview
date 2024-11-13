"""CLI to extract the most interesting 5 seconds from a song"""
#show examples - more examples and include example outputs in ReadMe
import librosa
import datetime
import sounddevice
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import click

def viz_songwaves(song_file_name):
    """Visualize the songwave amplitudes and frequency of a song"""
    sound, sr = librosa.load(song_file_name, sr=None)

    fig, ax = plt.subplots()
    librosa.display.waveshow(sound, sr=sr, ax=ax)
    ax.set(title='Soundwave amplitude of song over time')
    plt.xlabel('Time(seconds)')
    plt.ylabel('Amplitude')
    fig.savefig(f'visualizations/{song_file_name[6:-4]} soundwave_amplitude_visualization.jpg')

    fig, ax = plt.subplots()
    hop_length = 2048
    D = librosa.amplitude_to_db(np.abs(librosa.stft(sound, hop_length=hop_length)), ref=np.max)
    img = librosa.display.specshow(D, y_axis='log', sr=sr, hop_length=hop_length, x_axis='time', ax=ax)
    ax.set(title='Log-frequency power spectrogram')
    ax.label_outer()
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    fig.savefig(f'visualizations/{song_file_name[6:-4]} soundwave_log-frequency_visualization.jpg')

def viz_songnotes(song_file_name):
    """Visualize a song's most important notes and their frequency of a song"""
    sound, sr = librosa.load(song_file_name, sr=None)

    chroma = librosa.feature.chroma_stft(y=sound)

    fig, ax = plt.subplots()
    img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
    ax.set(title="Chromagram demonstration (Frequency of notes in song over time)")
    fig.colorbar(img, ax=ax)
    fig.savefig(f'visualizations/{song_file_name[6:-4]} song_notes.jpg')

    ccov = np.cov(chroma)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(ccov, y_axis='chroma', x_axis='chroma', ax=ax)
    ax.set(title='Chroma covariance')
    fig.colorbar(img, ax=ax)
    fig.savefig(f'visualizations/{song_file_name[6:-4]} important_song_notes.jpg')

def general_song_analysis(song_file_name):
    """Perform a general analysis of a song"""
    sound, sr = librosa.load(song_file_name, sr=None)

    tempo, beats = librosa.beat.beat_track(y=sound, sr=sr)
    length = librosa.get_duration(y=sound, sr=sr)

    print("The tempo of the song is: " + str(round(tempo[0])) + " BPM")
    print("The song length is: " + str(datetime.timedelta(seconds=round(length))))

def analyze_instruments(song_file_name):
    """Visualize the harmonic and percussive instruments used in a song."""
    sound, sr = librosa.load(song_file_name, sr=None)

    y_harmonic, y_percussive = librosa.effects.hpss(sound)

    fig, ax = plt.subplots()
    librosa.display.waveshow(y_harmonic, sr=sr, ax=ax)
    ax.set(title='Amplitude of the Harmonic Instrument Soundwaves Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    fig.savefig(f'visualizations/{song_file_name[6:-4]} harmonic_instrument_soundwaves.jpg')

    fig, ax = plt.subplots()
    librosa.display.waveshow(y_percussive, sr=sr, ax=ax)
    ax.set(title='Amplitude of the Percussive Instrument Soundwaves Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    fig.savefig(f'visualizations/{song_file_name[6:-4]} percussive_instrument_soundwaves.jpg')

def soundwave_analysis(song_file_name):
    """Extract the loudest 5 seconds of a song based on an analysis of its soundwaves."""
    file_name = song_file_name
    frame_length = 2048 #length of each frame used for RMS calculation. number of samples per frame
    hop_length = 512 #how much the analysis window moves for each frame
    n_seconds = 5

    sound, sr = librosa.load(file_name, sr = None) #sound is a 1D array of an audio signal. sr is the sampling rate (samples/s)

    #RMS (Root Mean Square) is a statistical measure used to represent the loudness of an audio signal. RMS calculates the 
    #square root of the average of the squared amplitudes of the signal, based on the number of samples. This essentially
    #quantifies the amplitude (volume) of an audio signal over time.
    clip_rms = librosa.feature.rms(y=sound, frame_length=frame_length, hop_length=hop_length) #RMS value is calculated for each frame
    clip_rms = clip_rms.squeeze() #2D array -> 1D array

    peak_rms_index = clip_rms.argmax() #finds the index of the highest RMS value (loudest frame in the song)
    peak_index = peak_rms_index*hop_length+int(frame_length/2) #sample index in the audio signal where the peak occurs

    half_slice_width = int(n_seconds*sr/2) #calculates half the width in samples of the desired audio slice
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
    default='CanoninD.mp3',
    type=str,
    help='Optional: Input file name of song to analyze. Defaults to CanoninD.'
)

def extract_five(
    song_file_name
):
    """Extract the most interesting 5 seconds from a song and perform further analysis on the song if desired."""
    song_file_name = f"songs/{song_file_name}"
    soundwave_analysis(song_file_name)
    viz_songwaves(song_file_name)
    viz_songnotes(song_file_name)
    general_song_analysis(song_file_name)
    analyze_instruments(song_file_name)

if __name__ == '__main__':
    main()

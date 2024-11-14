## Extracting the most significant 5 seconds from a song

### Description

- Command line interface built with Click
- `git clone https://github.com/rrachelhuangg/MusicNBrain_interview.git`
- `cd MusicNBrain_interview`

### Extracts the loudest 5 seconds of a song based on an analysis of its soundwaves using RMS. 

Running `python song_extraction.py extract_five --help` will display information about Click input formatting through the command line

[RMS](https://www.larsondavis.com/learn/sound-vibe-basics/sound-measurement-terminology) (Root Mean Square) is a statistical measure used to represent the loudness of an audio signal. RMS calculates the square root of the average
of the squared amplitudes of the signal, based on the number of samples. This essentially quantifies the amplitude (volume) of an audio signal over time.

RMS formula: <br/> <img width="200" alt="Screenshot 2024-11-13 at 11 06 37 AM" src="https://github.com/user-attachments/assets/0f0eaf72-1da9-4c45-9d2a-3ccb598da431">


### Testing the 5 second extraction
- Example Click commands for testing through the command line (the order of Click arguments does not matter):
  - `python song_extraction.py extract_five --song-file-name 'CanoninD.mp3'`
  
### Further analysis on other characteristics of the music can be performed

Currently, commenting/uncommenting the function calls in main will determine if visualizations of the other song characteristics are outputted. Characteristics that can be visualized (further analysis can be performed):

- Soundwave amplitude
<br/> ![CanoninD soundwave_amplitude_visualization](https://github.com/user-attachments/assets/827b6769-0997-40b6-b070-5efdd2f5cf1c)
- Soundwave frequency
<br/> ![CanoninD soundwave_log-frequency_visualization](https://github.com/user-attachments/assets/e4ffbe89-98aa-43e6-b4d8-1d3a6bc464bf)
- Frequency of songnotes
<br/>![CanoninD song_notes](https://github.com/user-attachments/assets/65a26c29-354a-49d8-86ee-dabb34ccd828)
- Most important songnotes
<br/>![CanoninD important_song_notes](https://github.com/user-attachments/assets/f509844c-6f3f-47e9-b300-fdb400818f35)
- Tempo
- BPM
- Instrument analysis: harmonic and percussive
<br/>![CanoninD harmonic_instrument_soundwaves](https://github.com/user-attachments/assets/41e608ad-6d7c-414b-adab-72ab055bc257)
<br/>![CanoninD percussive_instrument_soundwaves](https://github.com/user-attachments/assets/b6a5729c-b234-43c1-982c-8efa9ee45ce0)



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
  - `python song_extraction.py extract_five --song-file-name 'BillieJean.mp3'`
  
### Further analysis on other characteristics of the music can be performed

Currently, commenting/uncommenting the function calls in main will determine if visualizations of the other song characteristics are outputted. Characteristics that can be visualized (further analysis can be performed):

- Soundwave amplitude
- Soundwave frequency
- Frequency of songnotes
- Most important songnotes
- Tempo
- BPM
- Instrument analysis: harmonic and percussive

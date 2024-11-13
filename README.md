## Extracting the most significant 5 seconds from a song

### Description

- Command line interface built with Click
- `git clone https://github.com/rrachelhuangg/MusicNBrain_interview.git`
- `cd MusicNBrain_interview`

### Extracts the loudest 5 seconds of a song based on an analysis of its soundwaves using RMS. 

Running `python song_extraction.py extract_five --help` will display information about Click input formatting through the command line

[RMS](https://www.larsondavis.com/learn/sound-vibe-basics/sound-measurement-terminology) (Root Mean Square) is a statistical measure used to represent the loudness of an audio signal. RMS calculates the square root of the average
of the squared amplitudes of the signal, based on the number of samples. This essentially quantifies the amplitude (volume) of an audio signal over time.

RMS formula: 

### Testing the 5 second extraction
- Example Click commands for testing through the command line (the order of Click arguments does not matter):
  - `python song_extraction.py extract_five --song-file-name 'BillieJean.mp3'`
  
### Further analysis on other characteristics of the music can be performed

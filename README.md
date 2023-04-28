# Audio Features Based Playlist
### Generation of music playlists based on audio features analysis
The goal of this project is to generate audio playlists based on the precomputed audio features of a library of songs. For the analysis the Essentia library was used to extract features over the audio files contained in the MusAV dataset.

## MusAV Dataset
The [MusAV Dataset](https://github.com/MTG/musav-dataset) contains 2,092 30 seconds track previews covering 1,404 genres, with arousal and valence annotations.

## Features extraction
For the audio feature analysis the [Essentia](https://essentia.upf.edu/) library (open-source library from [Music Technology Group](https://www.upf.edu/web/mtg) at UPF) was used. For each audio file the extracted features are: BPM, danceability, wether it is a vocal or instrumental prominent track, a value for arausal and valence and a genre prediction.

The script uses several Essentia algorithms to perform the audio analysis, including `RhythmExtractor2013` for tempo analysis, `Danceability` for danceability analysis and several pretrained neural network models: `voice_instrumental-musicnn-msd-1.pb` for voice/instrumental classification, `msd-musicnn-1.pb` for arousal and valence analysis and `discogs-effnet-bs64-1.pb` for music style prediction.

Some other Essentia utilities such as `MonoLoader` for loading audio files are used.

## Included files
Included in this repository are a Python Notebook with the code for the features extraction (`AudioFeaturesBasedPlaylist.ipynb`), the result of the analysis of the 2100 MusAV audio files (`processed.csv`) and a [Streamlit](https://streamlit.io/) interface to generate the playlists (`Playlist_streamlit.py`).

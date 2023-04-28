import os
import streamlit as st
import pandas as pd

ESSENTIA_ANALYSIS_PATH = 'processed.csv'
NUM_TRACKS = 10

path = os.path.dirname(__file__)
os.chdir(path)

def load_essentia_analysis():
    return pd.read_csv(ESSENTIA_ANALYSIS_PATH, sep='\t')


st.title('Audio based playlist generator.')
df = load_essentia_analysis()
st.write(f'Using analysis data from {os.path.join(path,ESSENTIA_ANALYSIS_PATH)}')

st.write('## Analyzed data:')
st.write(df)

styles = df.MusicStyle.unique()
style_select = st.multiselect('Select a few music styles for your playlist:', styles)
# Exact match

bpm_select = st.selectbox('Select the tempo for your songs:', ['Slow','Medium','Fast'])
# Slow < 90 - Medium 90-120 - Fast 120-190

instrumental_select = st.selectbox('Do you want your songs to be vocal or instrumental?:', ['Vocal', 'Instrumental', 'Give me both!'])
# instrumental > 0.5, vocal > 0.5

danceability_select = st.slider('How danceable do you want the songs to be?', min_value = 0.0, max_value = 3.0, step = 0.1)
# danceability_select +-1

arousal_select = st.slider('Approx arousal value?:', min_value = 1.0, max_value = 9.0, step = 0.1)
# arousal_select +- 2

valence_select = st.slider('Approx valence value?', min_value = 1.0, max_value = 9.0, step = 0.1)
# valence_select +- 2


if st.button("RUN"):
    st.write('## 🔊 Results')

    if style_select:
        tempdf = df[df['MusicStyle'].isin(style_select)]

    if bpm_select:
        if bpm_select == 'Slow':
            tempdf = tempdf[tempdf['Tempo'] < 90]
        if bpm_select == 'Medium':
            tempdf = tempdf[(tempdf['Tempo'] > 90) & (tempdf['Tempo'] < 120)]
        if bpm_select == 'Fast':
            tempdf = tempdf[tempdf['Tempo'] > 120]

    

    # if style_rank:
    #     audio_analysis_query = audio_analysis.loc[mp3s][style_rank]
    #     audio_analysis_query['RANK'] = audio_analysis_query[style_rank[0]]
    #     for style in style_rank[1:]:
    #         audio_analysis_query['RANK'] *= audio_analysis_query[style]
    #     ranked = audio_analysis_query.sort_values(['RANK'], ascending=[False])
    #     ranked = ranked[['RANK'] + style_rank]
    #     mp3s = list(ranked.index)

    #     st.write('Applied ranking by audio style predictions.')
    #     st.write(ranked)

    # if max_tracks:
    #     mp3s = mp3s[:max_tracks]
    #     st.write('Using top', len(mp3s), 'tracks from the results.')

    # if shuffle:
    #     random.shuffle(mp3s)
    #     st.write('Applied random shuffle.')

    # # Store the M3U8 playlist.
    # with open(m3u_filepaths_file, 'w') as f:
    #     # Modify relative mp3 paths to make them accessible from the playlist folder.
    #     mp3_paths = [os.path.join('..', mp3) for mp3 in mp3s]
    #     f.write('\n'.join(mp3_paths))
    #     st.write(f'Stored M3U playlist (local filepaths) to `{m3u_filepaths_file}`.')

    # st.write('Audio previews for the first 10 results:')
    # for mp3 in mp3s[:10]:
    #     st.audio(mp3, format="audio/mp3", start_time=0)


st.text(str(style_select) + str(bpm_select) + str(instrumental_select))


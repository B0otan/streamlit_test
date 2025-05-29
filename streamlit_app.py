import streamlit as st

# Example mapping of songs to audio URLs or local file paths
song_dict = {
    "Shape of You - Ed Sheeran": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "Blinding Lights - The Weeknd": "https://www.youtube.com/watch?v=4NRXx6U8ABQ&ab_channel=TheWeekndVEVO",
    # Add more songs and their audio links here
}

songs = list(song_dict.keys())
selected_song = st.selectbox("🎵 Select your song:", songs)
st.write(f"**You selected:** {selected_song}")

# Display audio player for the selected song
audio_url = song_dict[selected_song]
st.audio(audio_url, format='audio/mp3')

import streamlit as st

st.title('🎵 Music Recommendation App')
st.write('Welcome to your personalized music space!')

# User input for artist or genre
music_input = st.text_input('Enter your favorite artist or genre:', '')

# Simple recommendations (replace or expand as needed)
recommendations = {
    'pop': [
        ('Taylor Swift - Shake It Off', 'https://www.youtube.com/watch?v=nfWlot6h_JM'),
        ('Ed Sheeran - Shape of You', 'https://www.youtube.com/watch?v=JGwWNGJdvx8'),
    ],
    'rock': [
        ('Queen - Bohemian Rhapsody', 'https://www.youtube.com/watch?v=fJ9rUzIMcZQ'),
        ('Nirvana - Smells Like Teen Spirit', 'https://www.youtube.com/watch?v=hTWKbfoikeg'),
    ],
    'jazz': [
        ('Miles Davis - So What', 'https://www.youtube.com/watch?v=zqNTltOGh5c'),
        ('John Coltrane - Giant Steps', 'https://www.youtube.com/watch?v=30FTr6G53VU'),
    ],
    'taylor swift': [
        ('Taylor Swift - Blank Space', 'https://www.youtube.com/watch?v=e-ORhEE9VVg'),
        ('Taylor Swift - Love Story', 'https://www.youtube.com/watch?v=8xg3vE8Ie_E'),
    ]
}

if music_input:
    genre = music_input.lower()
    st.subheader(f'Recommendations for "{music_input.title()}":')
    found = False
    for key in recommendations:
        if key in genre:
            for song, url in recommendations[key]:
                st.markdown(f"- [{song}]({url})")
            found = True
    if not found:
        st.info("Sorry, no recommendations found for your input. Try 'pop', 'rock', 'jazz', or an artist name!")
else:
    st.write('Enter an artist or genre above to get recommendations!')

st.write('---')
st.write('Created with ❤️ using Streamlit')

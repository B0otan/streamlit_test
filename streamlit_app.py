import streamlit as st
import requests

st.title('Currency Converter & Song Picker')

# --- Song Selection ---
songs = [
    "Shape of You - Ed Sheeran",
    "Blinding Lights - The Weeknd",
    "Despacito - Luis Fonsi",
    "Dance Monkey - Tones and I",
    "Perfect - Ed Sheeran",
    "Uptown Funk - Mark Ronson ft. Bruno Mars",
    "Someone You Loved - Lewis Capaldi",
    "Señorita - Shawn Mendes & Camila Cabello",
    "Sunflower - Post Malone & Swae Lee",
    "Rockstar - Post Malone ft. 21 Savage"
]
selected_song = st.selectbox("🎵 Select your song:", songs)
st.write(f"**You selected:** {selected_song}")

# --- Currency Conversion ---
@st.cache_data
def get_currency_codes():
    resp = requests.get('https://api.vatcomply.com/currencies')
    if resp.status_code == 200:
        return sorted(list(resp.json().keys()))
    else:
        return ['USD', 'EUR', 'MYR']

currency_codes = get_currency_codes()

base_currency = st.selectbox('From currency:', currency_codes, index=currency_codes.index('MYR') if 'MYR' in currency_codes else 0)
target_currency = st.selectbox('To currency:', currency_codes, index=currency_codes.index('USD') if 'USD' in currency_codes else 1)
amount = st.number_input('Amount:', min_value=0.0, value=1.0)

if st.button('Convert'):
    response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency}')
    if response.status_code == 200:
        rates = response.json().get('rates', {})
        if target_currency in rates:
            rate = rates[target_currency]
            converted = amount * rate
            st.success(f"{amount} {base_currency} = {converted:.2f} {target_currency}")
        else:
            st.error('Target currency not found.')
    else:
        st.error(f"API call failed with status code: {response.status_code}")

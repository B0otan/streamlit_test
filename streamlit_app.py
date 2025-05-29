import streamlit as st
import requests

st.title('Currency Converter')

# User input for amount and currency selection
amount = st.number_input('Enter amount:', min_value=0.0, value=1.0)
base_currency = st.text_input('From currency (e.g., MYR):', 'MYR')
target_currency = st.text_input('To currency (e.g., USD):', 'USD')

if st.button('Convert'):
    # Fetch exchange rates
    response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency.upper()}')
    if response.status_code == 200:
        rates = response.json().get('rates', {})
        if target_currency.upper() in rates:
            rate = rates[target_currency.upper()]
            converted = amount * rate
            st.write(f"{amount} {base_currency.upper()} = {converted:.2f} {target_currency.upper()}")
        else:
            st.error('Target currency not found in API response.')
    else:
        st.error(f"API call failed with status code: {response.status_code}")

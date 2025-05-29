import streamlit as st 
import requests

# Set the app title 
st.title('My First Streamlit App !!') 

# Add a welcome message 
st.write('Welcome to my Streamlit app!') 

# Create a text input for a custom message
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)

# Let user specify the base currency
base_currency = st.text_input('Enter a base currency code (e.g., USD, EUR, MYR):', 'USD')

#API call using user's input
if base_currency:
    response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency.upper()}')

    if response.status_code == 200:
        data = response.json()
        st.write('Exchange Rates Output:')
        st.json(data)  # nicely formatted JSON output
    else:
        st.error(f"API call failed with status code: {response.status_code}")
else:
    st.warning("Please enter a currency code.")

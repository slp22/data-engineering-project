"""
Streamlit Monkeypox Tweets MVP
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.write('''
# Monkeypox Tweets
#''')


st.write(
'''
Tweet Text
''')

tweets = pd.read_csv('tweets.csv')
tweets = tweets[['date', 'tweet']]
st.dataframe(tweets)


st.write(
'''
State Case Counts
'''
)

data = pd.read_csv('map_data.csv')
#data = data.rename(columns={'latitude': 'lat', 'longitude': 'lon'})

price_input = st.slider('Filter', int(data['cases'].min()), int(data['cases'].max()), 3500 )

price_filter = data['cases'] < price_input
st.map(data.loc[price_filter, ['lat', 'lon']])
st.markdown('Source: CDC 2022 U.S. Map & Case Count')
st.markdown('https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html')

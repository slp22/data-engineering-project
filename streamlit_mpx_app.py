"""
Streamlit Monkeypox Tweets MVP
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.write('''
# Monkeypox Tweets
#''')
st.title('Title')



st.write(
'''
## Tweet Text
''')
st.subheader('Subheader')


tweets = pd.read_csv('tweets.csv')
tweets = tweets[['date', 'tweet']]
st.dataframe(tweets)


st.write(
'''
## State Case Counts
'''
)
st.subheader('Subheader')


data = pd.read_csv('map_data.csv')

input = st.slider('Filter', int(data['cases'].min()), int(data['cases'].max()), 3500 )
st.caption('Caption')


filter = data['cases'] < input
st.map(data.loc[filter, ['lat', 'lon']])
st.markdown('Source: [CDC 2022 U.S. Map & Case Count](https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html)')

st.caption('Caption')
#st.write(mpl_fig) : Displays a Matplotlib figure


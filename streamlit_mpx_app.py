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
## Tweet Text
''')

tweets = pd.read_csv('tweets.csv')
tweets = tweets[['date', 'tweet']]
st.dataframe(tweets)


st.write(
'''
## State Case Counts
'''
)

data = pd.read_csv('map_data.csv')

input = st.slider('Filter', int(data['cases'].min()), int(data['cases'].max()), 3500 )

filter = data['cases'] < input
st.map(data.loc[filter, ['lat', 'lon']])
st.markdown('Source: [CDC 2022 U.S. Map & Case Count](https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html)')

st.title('Title')
st.header('Header')
st.subheader('Subheader')
st.caption('This is a string that explains something above.')
#st.write(mpl_fig) : Displays a Matplotlib figure


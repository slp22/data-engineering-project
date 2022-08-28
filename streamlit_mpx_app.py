"""
Streamlit Monkeypox Tweets MVP
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.write('''
# Monkeypox Tweets
#''')
#
#
## PART 2 - Markdown Syntax
#
#st.write(
#'''
#
### PART 3 - Table
#
st.write(
'''
Tweet Text
''')

tweets = pd.read_csv('tweets.csv')
tweets = tweets[['date', 'tweet']]
st.dataframe(tweets)


## PART 4 - Graphing and Buttons
#
#st.write(
#'''
#### Graphing and Buttons
#Let's graph some of our data with matplotlib. We can also add buttons to add interactivity to our app.
#'''
#)
#
#fig, ax = plt.subplots()
#
#ax.hist(data['PRICE'])
#ax.set_title('Distribution of House Prices in $100,000s')
#
#show_graph = st.checkbox('Show Graph', value=True)
#
#if show_graph:
#     st.pyplot(fig)
#
#
# PART 5 - Mapping and Filtering Data

st.write(
'''
Mapping and Filtering Data
'''
)

#map_data = pd.read_csv('map_data.csv')
#
#case_input = st.slider('Filter', int(map_data['cases'].min()), int(map_data['cases'].max()), 4000)
#
#case_filter = map_data['cases'] < case_input
#st.map(map_data.loc[case_filter, ['lat', 'long']])

data = pd.read_csv('map_data.csv')
data = data.rename(columns={'latitude': 'lat', 'longitude': 'lon'})

price_input = st.slider('Filter', int(data['case count'].min()), int(data['case count'].max()), 3500 )

price_filter = data['case count'] < price_input
st.map(data.loc[price_filter, ['lat', 'lon']])

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

data = pd.read_csv('tweets.csv')
data = data[['date', 'tweet']]
st.dataframe(data)


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
## PART 5 - Mapping and Filtering Data
#
#st.write(
#'''
#Mapping and Filtering Data
#'''
#)
#
#price_input = st.slider('House Price Filter', int(data['PRICE'].min()), int(data['PRICE'].max()), 500000 )
#
#price_filter = data['PRICE'] < price_input
#st.map(data.loc[price_filter, ['lat', 'lon']])
#
#

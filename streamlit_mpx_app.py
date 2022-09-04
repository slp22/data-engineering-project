"""
Streamlit Monkeypox Tweets MVP
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.write('''# Monkeypox Tweets''')

st.write(
'''## Tweet Text''')

tweets = pd.read_csv('tweets.csv')
tweets = tweets[['date', 'tweet']]
st.dataframe(tweets)

st.write(
'''## State Case Counts''')

data = pd.read_csv('map_data.csv')

input = st.slider('?', int(data['cases'].min()),int(data['cases'].max()), 3500 )

filter = data['cases'] < input
st.map(data.loc[filter, ['lat', 'lon']])
st.markdown('Source: [CDC 2022 U.S. Map & Case Count](https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html)')



st.metric(label="Temperature", value="70 °F", delta="1.2 °F")


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


st.metric(label="Gas price", value=4, delta=-0.5,
     delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
     delta_color="off")
     
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

#st.write(mpl_fig) : Displays a Matplotlib figure


"""
Streamlit Monkeypox Tweets MVP
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud






col1, col2 = st.columns(2)

# ----Topic Word Cloud----
with col1:
    st.header("Topic Word Cloud")

    topic1 = 'emergency, global, spreading, cdc, biden, pandemic, said, risk, day, yet, even, may, could, government, coming, children, fear, foxnews, states, stop'
    topic2 = 'vaccine, smallpox, cdc, vaccines, shingles, yet, day, states, risk, everyone, vax, make, foxnews, biden, also, many, even, government, really, since'
    topic3 = 'gay, men, sex, community, spreading, aids, cdc, stop, contact, man, children, month, risk, say, way, said, anyone, everyone, since, many'
    topic4 = 'cnn, biden, trump, real, democrats, states, make, msnbc, good, years, man, please, said, since, day, never, let, right, say, even'
    topic5 = 'dont, pandemic, see, moneypox, well, im, still, right, say, vaccines, even, thing, back, way, good, really, stop, biden, make, coming'

    topic = st.selectbox('Select topic:',['risk','vaccine','gay men', 'news', 'mix'])

    def create_wordcloud(topic):
        if topic == 'risk':
            topic = topic1
        elif topic == 'vaccine':
            topic = topic2
        elif topic == 'gay men':
            topic = topic3
        elif topic == 'news':
            topic = topic4
        else:
            topic = topic5

        wordcloud = WordCloud().generate(topic)
        return wordcloud

    wordcloud = create_wordcloud(topic)

    fig, ax = plt.subplots(figsize = (12, 12))
    ax.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig)

# ----Tweets by Date----
@st.cache
def load_date_data():
    data = pd.read_csv('date_df.csv')
    return data

with col2:
    st.header("Tweets by Date")
    date_data = load_date_data()
    date_df = pd.DataFrame(date_data, columns = ['date', 'tweets_per_day'])
    st.line_chart(date_df, x='date', y='tweets_per_day')

# ----Tweet Text----
with col2:
    st.header("Monkeypox Tweets")

    tweets = pd.read_csv('tweets.csv')
    tweets = tweets[['date', 'text']]
    st.dataframe(tweets)


# ----State Case Counts----
with col1:
    st.header("State Case Counts")

    data = pd.read_csv('state_cases_for_map.csv')
    input = st.slider('Slide for state counts:', int(data['cases'].min()),int(data['cases'].max()), 3500 )
    filter = data['cases'] < input
    st.map(data.loc[filter, ['lat', 'lon']])
    st.markdown('Source: [CDC 2022 U.S. Map & Case Count](https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html)')

# ----Tweet Metrics----
with col1:
    st.header("Tweet Metrics")

    st.metric(label="Tweets", value="197,594")
with col2:
    st.metric(label="Handles", value="15,990")

    



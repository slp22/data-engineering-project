"""
Streamlit Monkeypox Tweets MVP
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud



st.write('''# Monkeypox Tweets''')

#st.write('''## Tweet Topics ''')
#topics = pd.read_csv('topics_df.csv')
#topics = topics[[]]



st.write(
'''## Tweet Text''')

tweets = pd.read_csv('tweets_2.csv')
tweets = tweets[['date', 'text']]
st.dataframe(tweets)

st.write(
'''## State Case Counts''')

data = pd.read_csv('state_cases_for_map.csv')

input = st.slider('?', int(data['cases'].min()),int(data['cases'].max()), 3500 )

filter = data['cases'] < input
st.map(data.loc[filter, ['lat', 'lon']])
st.markdown('Source: [CDC 2022 U.S. Map & Case Count](https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html)')



st.write('''# cloud 1''')

# text
cloud = pd.read_csv('words_for_cloud.txt')

# Create and generate a word cloud image:
wordcloud_1 = WordCloud().generate(cloud)


# Display the generated image:
fig, ax = plt.plot(figsize = (12, 8))
ax.imshow(wordcloud_1) #, interpolation='bilinear')
plt.axis("off")
st.pyplot(fig)





st.write('''# cloud 2''')


# Create text
topic1 = 'emergency, global, pandemic, spreading, biden, cdc, said, risk, even, well, may, day, right, coming, could'
topic2 = 'vaccine, smallpox, vaccines, cdc, shingles, day, well, im, yet, even, biden, moneypox, make, states, dont'
topic3 = 'gay, men, sex, cnn, dont, spreading, stop, say, community, aids, right, cdc, see, pandemic, man'

topic = st.selectbox('select topic',['topic1','topic2','topic3'])

# Create and generate a word cloud image:
def create_wordcloud(topic):
    if topic == 'topic1':
        topic = topic1
    elif topic == 'topic2':
        topic = topic2
    else:
        topic = topic3

    wordcloud = WordCloud().generate(topic)
    return wordcloud

wordcloud_2 = create_wordcloud(topic)

# Display the generated image:
fig, ax = plt.subplots(figsize = (12, 8))
ax.imshow(wordcloud_2)
plt.axis("off")
st.pyplot(fig)




#st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
#
#
#col1, col2, col3 = st.columns(3)
#col1.metric("Temperature", "70 °F", "1.2 °F")
#col2.metric("Wind", "9 mph", "-8%")
#col3.metric("Humidity", "86%", "4%")
#
#
#st.metric(label="Gas price", value=4, delta=-0.5,
#     delta_color="inverse")
#
#st.metric(label="Active developers", value=123, delta=123,
#     delta_color="off")
#
#df = pd.DataFrame(
#    np.random.randn(10, 5),
#    columns=('col %d' % i for i in range(5)))
#

#st.write(mpl_fig) : Displays a Matplotlib figure


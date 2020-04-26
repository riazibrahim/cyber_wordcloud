from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('/home/soze/coding/24-cyber_cloud/Youtube04-Eminem.csv')
comment_words = ''
stop_words = set(STOPWORDS)

for val in df.CONTENT:
    val = str(val)
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens)

wordcloud = WordCloud(width=800, height=800,
                       background_color='white',
                       stopwords=stop_words,
                       min_font_size=10).generate(comment_words)

plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)

# plt.show()
plt.savefig('figure.png')


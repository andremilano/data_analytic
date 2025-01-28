import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Langkah 1: Memuat data yang telah dibersihkan
df = pd.read_csv('result/cleaned_tweets.csv')  # Pastikan file ini sudah ada dan berisi data yang telah dibersihkan

# Langkah 2: Gabungkan semua tweet yang telah dibersihkan
all_tweets = ' '.join(df['cleaned_text'].tolist())

# Langkah 3: Buat word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_tweets)

# Langkah 4: Tampilkan word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
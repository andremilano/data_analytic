import pandas as pd
from textblob import TextBlob

# Langkah 1: Memuat data yang telah dibersihkan
df = pd.read_csv('result/cleaned_tweets.csv')  # Pastikan file ini sudah ada dan berisi data yang telah dibersihkan

# Langkah 2: Fungsi untuk mendapatkan sentiment
def get_sentiment(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

# Langkah 3: Apply fungsi get_sentiment ke kolom cleaned_tweet
df['sentiment'] = df['cleaned_text'].apply(get_sentiment)

# Langkah 4: Klasifikasikan sentiment sebagai positif, netral, atau negatif
df['sentiment_category'] = df['sentiment'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))

# Langkah 5: Simpan data dengan sentiment analysis
df.to_csv('result/tweet_data_with_sentiments.csv', index=False)

# Langkah 6: Tampilkan hasil sentiment analysis
print(df[['cleaned_text', 'sentiment', 'sentiment_category']].head())
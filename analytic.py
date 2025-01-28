from collections import Counter
import nltk
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt

# Langkah 1: Membaca data
df = pd.read_csv('result/cleaned_tweets.csv')  # Pastikan file ini sudah ada

# Langkah 2: Download stopwords jika belum ada
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Langkah 3: Gabungkan semua tweet yang telah dibersihkan
all_tweets = ' '.join(df['cleaned_text'].tolist())

# Langkah 4: Tokenisasi dan hitung frekuensi kata
words = all_tweets.split()
filtered_words = [word for word in words if word.lower() not in stop_words]
word_freq = Counter(filtered_words)

# Langkah 5: Ambil 10 kata paling umum
top_10_words = word_freq.most_common(10)

# Langkah 6: Pisahkan kata dan frekuensi untuk visualisasi
words, frequencies = zip(*top_10_words)

# Langkah 7: Visualisasi menggunakan matplotlib
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.title('Top 10 Most Common Words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)  # Rotasi label sumbu x agar lebih mudah dibaca
plt.show()
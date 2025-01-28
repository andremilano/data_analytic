import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Langkah 1: Memuat data yang telah dianalisis sentimennya
df = pd.read_csv('result/tweet_data_with_sentiments.csv')  # Pastikan file ini sudah ada

# Langkah 2: Hitung jumlah sentiment
sentiment_counts = df['sentiment_category'].value_counts()

# Langkah 3: Buat bar plot menggunakan seaborn
plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
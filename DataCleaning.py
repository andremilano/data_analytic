import pandas as pd
import re

# Load data dari file CSV hasil crawling
data = pd.read_csv('data/jkt48.csv')

# Menghapus duplikat tweet
data = data.drop_duplicates(subset=['full_text'])

# Fungsi untuk membersihkan teks
def clean_text(text):
    # Menghapus URL
    text = re.sub(r'http\S+', '', text)
    # Menghapus mention (@username)
    text = re.sub(r'@\w+', '', text)
    # Menghapus hashtag
    text = re.sub(r'#\w+', '', text)
    # Menghapus karakter non-alfanumerik
    text = re.sub(r'[^\w\s]', '', text)
    # Menghapus spasi berlebih
    text = ' '.join(text.split())
    return text

# Membersihkan kolom 'full_text'
data['cleaned_text'] = data['full_text'].apply(clean_text)

# Menyimpan data yang telah dibersihkan
data.to_csv('result/cleaned_tweets.csv', index=False)
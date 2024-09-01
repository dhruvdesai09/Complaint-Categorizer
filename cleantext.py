import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preprocess_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Join words back into a single string
    cleaned_text = ' '.join(filtered_words)

    return cleaned_text

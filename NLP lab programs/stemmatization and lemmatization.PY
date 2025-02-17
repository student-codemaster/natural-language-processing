import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
corpus=[
    "The cats are running.",
    "He was running faster than the other competitors.",
    "I love to watch dogs play.",
    "The leaves are falling down",
]
stemmer=PorterStemmer()
lemmatizer=WordNetLemmatizer()
def stem_words(text):
    words=word_tokenize(text)
    return[stemmer.stem(word) for word in words]
def lemmatize_words(text):
    words=word_tokenize(text)
    return[lemmatizer.lemmatize(word) for word in words]
for sentence in corpus:
    print(f"original:{sentence}")
    print(f"stemmed:{stem_words(sentence)}")
    print(f"lemmatizer:{lemmatize_words(sentence)}")
    print("-"*40)
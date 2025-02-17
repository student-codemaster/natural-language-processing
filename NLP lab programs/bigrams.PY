import nltk
from nltk import bigrams
from collections import Counter
nltk.download('punkt')
sentences =[
    'i love programming'
    'programming is fun '
    'i lov learning new things'

]
tokenized_sentence = [nltk.word_tokenize(sentence.lower()) for sentence in sentences ]
all_bigrams=[]
for tokens in tokenized_sentence:
    all_bigrams.extend(bigrams(tokens))

bigram_counts = Counter(all_bigrams)

for bigram,count in bigram_counts.items():
    print(f'{bigram}:{count}')
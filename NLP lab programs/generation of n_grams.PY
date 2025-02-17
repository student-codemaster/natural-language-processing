import nltk
from nltk import ngrams
Text = 'natural language is an indiciplinary subfield of liguistics and computer science'

def genereate_ngrams(Text,words_numbers):
  words = Text.split()
  output=[]
  for i in range(len(words)-words_numbers+1):
    output.append(words[i:i+words_numbers])
  return output
genereate_ngrams(Text,words_numbers=1)

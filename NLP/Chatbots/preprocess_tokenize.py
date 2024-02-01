# this is a standard preprocessing function:
# tokenizes, removes stopwords and creates a list of tokens from a text.

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
                 
def preprocess(input_sentence):
    input_sentence = input_sentence.lower()
    input_sentence = re.sub(r'[^\w\s]','',input_sentence)
    tokens = word_tokenize(input_sentence)
    input_sentence = [i for i in tokens if not i in stop_words]
    return(input_sentence)

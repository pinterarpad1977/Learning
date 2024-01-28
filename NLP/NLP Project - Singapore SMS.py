import pandas as pd
import re
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.stem import WordNetLemmatizer

def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
  pos_counts = Counter()
  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech

normalizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))
df = pd.read_csv('clean_nus_sms.csv')
raw_messages = list(df['Message'])

# create a list of regex cleaned messages and a single string for the appended cleaned messages
cleaned_messages = []
text_only = ""
for message in raw_messages:
    msg_str = str(message)
    cleaned = re.sub(r'\W+',' ',msg_str).lower().strip()
    cleaned_messages.append(cleaned)
    text_only += cleaned+' '

# remove stop words from  the list of messages
messages = [word for word in cleaned_messages if word not in stop_words]

# tokenize the merged text and remove stop words
raw_tokenized = word_tokenize(text_only)
tokenized = [token for token in raw_tokenized if token not in stop_words]

token_counter = Counter
token_counts = token_counter(tokenized)
print(token_counts.most_common(20),'\n')

# Normalize the tokenized text to return root of the words based on the the part of speech
normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

normalized_counter = Counter
normalized_counts = normalized_counter(normalized)

print(normalized_counts.most_common(20))

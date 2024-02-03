import numpy as np
import re
from twitter_prep import pairs

# Building empty lists to hold sentences
input_docs = []
target_docs = []
# Building empty vocabulary sets
input_tokens = set()
target_tokens = set()

for line in pairs[:15]:
  # Input and target sentences are in a list of tuples
  input_doc, target_doc = line[0], line[1]
  # Appending each input sentence to input_docs
  # according to Chat-GPT we need to keep the input_docs untouched, that is why the regex is not applied on them
  input_docs.append(input_doc)
  # Splitting words from punctuation in the target_docs
  target_doc = " ".join(re.findall(r"[\w']+|[^\s\w]", target_doc))
  # We indicate the start and end of each target_doc:
  target_doc = '<START> ' + target_doc + ' <END>'
  target_docs.append(target_doc)
  
  # Now we split up each sentence into words and add each unique word to our vocabulary set
  for token in re.findall(r"[\w']+|[^\s\w]", input_doc):
    if token not in input_tokens:
      input_tokens.add(token)
  for token in target_doc.split():
    if token not in target_tokens:
      target_tokens.add(token)

input_tokens = sorted(list(input_tokens))
target_tokens = sorted(list(target_tokens))

# Create num_encoder_tokens and num_decoder_tokens:
num_encoder_tokens = len(input_tokens)
num_decoder_tokens = len(target_tokens)

max_encoder_seq_length = max([len(re.findall(r"[\w']+|[^\s\w]", input_doc)) for input_doc in input_docs])
max_decoder_seq_length = max([len(re.findall(r"[\w']+|[^\s\w]", target_doc)) for target_doc in target_docs])

# enumerate creates an iterable with the index of an item and the item itself
# NOTE that it is swapped when added to the dictionary, so the the item is the key and its index is the value
input_features_dict = dict(
    [(token, i) for i, token in enumerate(input_tokens)])
target_features_dict = dict(
    [(token, i) for i, token in enumerate(target_tokens)])

# another swap of keys and values in the reverse dictionaries
reverse_input_features_dict = dict(
    (i, token) for token, i in input_features_dict.items())
reverse_target_features_dict = dict(
    (i, token) for token, i in target_features_dict.items())

encoder_input_data = np.zeros(
    (len(input_docs), max_encoder_seq_length, num_encoder_tokens),
    dtype='float32')
decoder_input_data = np.zeros(
    (len(input_docs), max_decoder_seq_length, num_decoder_tokens),
    dtype='float32')
decoder_target_data = np.zeros(
    (len(input_docs), max_decoder_seq_length, num_decoder_tokens),
    dtype='float32')

# enumerate(zip()) creates an iterable of sets with their indexes
# line is the index and (iput_doc, target_doc) is the item (a set)
for line, (input_doc, target_doc) in enumerate(zip(input_docs, target_docs)):

  # another enumerate gives back the index of the words returned by the regex and the word
  # input_docs go to the encoder_input_data
  for timestep, token in enumerate(re.findall(r"[\w']+|[^\s\w]", input_doc)):
    # Assign 1. for the current line, timestep, & word in encoder_input_data -> this will create the one-hot vector for the token
    encoder_input_data[line, timestep, input_features_dict[token]] = 1.

  # target_docs go to the decoder_input_data
  for timestep, token in enumerate(target_doc.split()):
    decoder_input_data[line, timestep, target_features_dict[token]] = 1.
    if timestep > 0:
      # decoder_target_data is ahead by 1 timestep and doesn't include the start token.
      decoder_target_data[line, timestep - 1, target_features_dict[token]] = 1.
'''
print(f'input_docs: {len(input_docs)}')
print(f'target_docs: {len(target_docs)}')
print(f'input_tokens: {len(input_tokens)}')
print(f'target_tokens: {len(target_tokens)}')
print(f'max_encoder_seq_length: {max_encoder_seq_length}')
print(f'max_decoder_seq_length {max_decoder_seq_length}')
'''
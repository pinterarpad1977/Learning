from itertools import zip_longest
import re
import os

script_dir = os.path.dirname(__file__)
rel_path = "weather.txt"
abs_path = os.path.join(script_dir,rel_path)

# Defining lines as a list of each line
with open(abs_path, 'r', encoding='utf-8') as f:
  lines = f.read().split('\n')

lines = [re.sub(r"(?:\@|https?\://)\S+", "", line).strip() for line in lines]

# group lines by response pair

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
pairs = list(grouper(lines, 2))
#print(pairs)
#print(type(pairs[0]))
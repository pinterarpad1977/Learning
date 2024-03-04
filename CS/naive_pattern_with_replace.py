def pattern_search(text, pattern, replacement, case_sensitive=True):
  fixed_text = ""
  num_skips = 0

  for index in range(len(text)):

    if num_skips > 0:
      num_skips -= 1
      continue

    match_count = 0

    for char in range(len(pattern)): 
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break

    if match_count == len(pattern):
      print(pattern, "found at index", index)
      fixed_text += replacement
      num_skips = len(pattern)-1
    else:
      fixed_text += text[index]

  return fixed_text

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language", "language")
pattern_search(friends_intro, "pylhon", "Python", False)
pattern_search(friends_intro, "idil", "ideal", False)
pattern_search(friends_intro, "zzz ", "")
pattern_search(friends_intro, "syntacs", "syntax")
pattern_search(friends_intro, "languuUuage", "language")

'''
The first step is to create a fixed_text placeholder that will act as a safe copy of the original text and build this duplicate out character-by-character. 
This is needed to prevent out-of-bounds errors related to changing the length of the text being iterated. 
Adding in replacement patterns means that the following characters from the original text should no longer be copied over, as to not overwrite the replacement. 
Luckily, as the pattern is the item being replaced, 
we can use its length to determine the amount of search iterations to skip using the continue keyword. 
1 must be subtracted from this length to account for the replacement of the current character. '''

#!/usr/bin/env python
import sys

curr_count = 0
word_dict = {}

# Process each key-value pair from the mapper
for line in sys.stdin:

    # Get the key and value from the current line
    word, count, f_name = line.rstrip().split(',')

    # Getting only the file name.
    f_name = f_name.split('/')[-1]
    # Convert the count to an int
    count = int(count)
    if word in word_dict.keys():
        word_dict[word][0] += 1
    else:
        word_dict[word] = [1, f_name]

for key in word_dict.keys():
    print '{},{},{}'.format(key, word_dict[key][0],word_dict[key][1])

#!/usr/bin/env python

import sys
import numpy as np

word_dict, dups = {}, {}

for line in sys.stdin:
    elements = line.rstrip().split(',')
    tf_idf = float(int(elements[1])*float(elements[3]))
    # Key is the tf_idf, values are the word and the doc id
    try:
        word_dict[tf_idf] = [elements[0], elements[2]]
    except:
        dups[tf_idf] = [elements[0], elements[2]]

sorted_tfidf = sorted(word_dict, reverse = True)[:20]

for k in sorted_tfidf:
    print '{},{},{}'.format(k, word_dict[k][0], word_dict[k][1])
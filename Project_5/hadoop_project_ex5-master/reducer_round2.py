#!/usr/bin/env python
# Compute the idf

import sys
import numpy as np

words_dict, list_docs = {}, []

for line in sys.stdin:
    word, count, doc_id = line.rstrip().split(",")
    if word in words_dict.keys():
        list_len = len(words_dict[word])
        words_dict[word][list_len-1] += 1
    else:
        words_dict[word] = [word, count, doc_id, 1]
    if doc_id in list_docs:
        pass
    else:
        list_docs.append(doc_id)

n = len(list_docs)

for k, v in words_dict.iteritems():
    last_item = len(words_dict[k])
    idf_t =  np.log(n/float(v[3]))
    print "{},{},{},{},{}".format(v[0], v[1], v[2], v[3], idf_t)
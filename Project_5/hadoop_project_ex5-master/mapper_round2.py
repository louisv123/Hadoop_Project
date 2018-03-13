#!/usr/bin/env python
# For computing document frequency.

import sys
import os

for line in sys.stdin:
    try:
        word, count, id = line.rstrip().split(",")
        print "{},{},{}".format(word, count, id)
    except:
        pass



#!/usr/bin/env python

import sys
import numpy as np

for line in sys.stdin:
    elements = line.rstrip().split(',')
    print '{},{},{},{}'.format(elements[0], elements[1],
                               elements[2], elements[4])
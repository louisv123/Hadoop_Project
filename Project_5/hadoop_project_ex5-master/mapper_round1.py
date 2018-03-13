#!/usr/bin/env python

#!/usr/bin/env python
import sys
import os
import string

# Read each line from stdin
for line in sys.stdin:
    # Lowering the line
    line = line.lower().translate(None, string.punctuation)
    words = line.split()
    # Generate the count for each word
    for word in words:
    # Write the key-value pair to stdout to be processed by
    # the reducer.
    # The key is anything before the first tab character and the
    #value is anything after the first tab character.
        print '{},{},{}'.format(word, 1, os.environ['mapreduce_map_input_file'])
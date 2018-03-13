#!/usr/bin/env python
#job 1

#mapper_1
import os
import sys


for line in sys.stdin:
	#for each line node1	node2 and convert into (node1,node2)
	nodes = line.split()
	print '{},{}'.format(nodes[0],nodes[1])




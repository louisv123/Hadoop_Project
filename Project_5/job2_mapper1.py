#!/usr/bin/env python
#job 2
#mapper_1

import sys

for line in sys.stdin:


	node_1, nodes = line.rstrip().split(';')

	for link in nodes[:-1]:
		#print out of link, page rank, length of out link of initial node
		print '{},{},{}'.format(link,nodes[-1],nodes[:-1].length)

	# print in link, and out link
	print '{};{}'.format(node_1,nodes[:-1])
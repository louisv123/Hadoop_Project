#!/usr/bin/env python
#job 2
#mapper_1

import sys

for line in sys.stdin:


	node_1, page_rank, nodes = line.rstrip().split(';')

	for link in nodes.split(","):
		link=link.replace("[","")
		link=link.replace(']','')

		if link!="":
			#print out of link, page rank, length of out link of initial node
			print '{},{},{}'.format(link,page_rank,len(nodes.split(",")))
	
	# print in link, and out link
	if nodes!='[]':
		print '{};{}'.format(node_1,nodes)
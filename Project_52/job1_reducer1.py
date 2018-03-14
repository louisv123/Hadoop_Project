#!/usr/bin/env python
#job 1

#reducer_1
import sys

node_link={}

for line in sys.stdin:

	#from (node1, node2) we compute (node1,page_rank,node1_out1, node1_out2,...)

	#get the node 1 node 2 and the file name
	node_1, node_2=line.rstrip().split(',')
	
	

	if node_1 in node_link.keys():
		node_link[node_1].append(int(node_2))
	else:
		node_link[node_1]=[int(node_2)]

for key in node_link.keys():
	node_link[key].append(0.85/len(node_link.keys()))
	print '{};{};{}'.format(key,node_link[key][-1],node_link[key][:-1])
	
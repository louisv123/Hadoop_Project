#!/usr/bin/env python
#job 2
 
#reducer_1

import sys
import argparse

new_page_rank={}
for line in sys.stdin:

	

	if len(line.split(';'))==2:
	
		node, value = line.rstrip().split(';')

		node=int(node)

		value=value.replace("[","").replace("'","").replace("]","")
		value=map(int,value.split(","))
		

		if node in new_page_rank.keys():
			new_page_rank[node][1]=new_page_rank[node][1]+value
		else:
			new_page_rank[node]=[0,value]
	
	else:

		node, page_rank, nbr_out_link = line.rstrip().split(",")
		
		node=int(node.replace("'",""))

		if node in new_page_rank.keys():
			new_page_rank[node][0]+=float(page_rank)/float(nbr_out_link)
		
		else:
			new_page_rank[node]=[float(page_rank)/float(nbr_out_link),[]]
		
for key in new_page_rank.keys():
	
	page_rank=(1-0.85)/len(new_page_rank.keys())+0.85*new_page_rank[key][0]
	
	print '{};{};{}'.format(key,page_rank,new_page_rank[key][1])
	




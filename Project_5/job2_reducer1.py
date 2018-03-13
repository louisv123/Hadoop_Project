#!/usr/bin/env python
#job 2
 
#reducer_1

import sys
new_page_rank={}
for line in sys.stdin:

	

	if len(line.split(';'))==2:
	
		node, value = line.rstrip().split(';')

		if node in new_page_rank.keys():
			new_page_rank[node].append(value)
		else
			new_page_rank[node]=[0,value]
	
	else:

		node, page_rank, nbr_out_link = line.rstrip().split(",")
		
		if node in new_page_rank.keys():
			new_page_rank[node][0]=0.85*((new_page_rank[node][0]-(1-0.85))/0.85+page_rank/nbr_out_link)+(1-0.85)
		else:
			new_page_rank[node]=[0.85*page_rank/nbr_out_link+(1-0.85)]
		
for key in new_page_rank.keys():

	print '{};{},{}'.format(key,new_page_rank[node][0],new_page_rank[node][1:])






## PAGE RANK

### Job 1 :

The job 1 initializes each node with a page rank equals to 0.85/#nodes.

- mapper takes as input "node1 node2" and gives as output "node1","node2"

- reducer takes as input "node1","node2" and gives as output 
"node1",0.85/#nodes,"node1_out1,...,node1_outn"



### Job 2 :

The job 2 computes one iteration of the page rank algorithm:

- mapper takes as input "node1, page_rank_of_node1, "node1_out1,...,node1_outn" and gives two outputs:

	- "node1", "node1_out1,...,node1_outn" 
  
  - for each node1_out:
      "node_1_outi", "page_rank_of_node1", "# of_out_link_from_1"
      
 - reducer takes as input either  "node1", "node1_out1,...,node1_outn"  or node_1_outi, page_rank1, # of_out_link_from_1.
   He gives as output "node1", "new_page_rank_of_node1", "node1_out1,...,node1_outn" 
   
#### Example:

![alt text](https://github.com/louisv123/Hadoop_Project/blob/master/Project_5/Picture/Capture1.png?raw=true)

 - Job 1:
 
For the mapper, one has:
"1","2"

"2","3"

"3","1"

"3","2"

...

For the reducer, the page_rank = 0.85/5 =0.17

we would have:

"1","0.17","2"

"2","0.17","3"

"3","0.17","1,2,4"

...

  - Job 2
 
 For the mapper, we have two outputs:
 
  - The first output for 1 is the "out_link_from_1", the "page_rank" and the #nodes from 1:
  	
	"2","0.17","1"
	
  - The second output for 1 is "1" and "1_out1,...,1_outn":
  	
	"1","2"
 

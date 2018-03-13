## PAGE RANK

### Job 1 :

The job 1 initializes each node with a page rank equals to 0.85/#nodes.

- mapper takes as input "node1 node2" and gives as output "node1","node2"

- reducer takes as input "node1","node2" and gives as output 
"node1",0.85/#nodes,"node1_out1,...,node1_outn"

#### Example:

![alt text](https://github.com/louisv123/Hadoop_Project/blob/master/Project_5/Picture/Capture1.png?raw=true)

here, we would have:
"1","0.17","2,3"
"2","0.17","1,3,4"

### Job 2 :

The job 2 computes one iteration of the page rank algorithm:

- mapper takes as input "node1, page_rank_of_node1, "node1_out1,...,node1_outn" and gives two outputs:

	- "node1", "node1_out1,...,node1_outn" 
  
  - for each node1_out:
      "node_1_outi", "page_rank_of_node1", "# of_out_link_from_1"
      
 - reducer takes as input either  "node1", "node1_out1,...,node1_outn"  or node_1_outi, page_rank1, # of_out_link_from_1.
   He gives as output "node1", "new_page_rank_of_node1", "node1_out1,...,node1_outn" 
   

# Social Network
## Dataset Specification:
1. Social Circle : Facebook (UNDIRECTED EDGES)
2. Wikipedia Vote Network (DIRECTED EDGES)
## Programming languages
Python
#### Package
Networkx: https://networkx.org/documentation/stable/tutorial.html
## Project Round 1
#### Problem Statement 1:
Find all centrality measures, clustering coefficients (both local and global) and reciprocity and transitivity. We have studied in the class using appropriate algorithms (you may use specific packages for this or write your own algorithm for the same). 

#### Problem Statement 2:
Try to get an algorithm package in Python to find the maximum connected component (called a giant component in the class) in a given graph G. Let us denote the number of nodes in the giant component of a graph G as N_G. Vary ⟨k⟩ from 0 to 5 with increment of 0.1. For each value of ⟨k⟩ find the ratio N_G/N where N is the number of nodes in the graph. Plot this ratio with respect to ⟨k⟩. Take ⟨k⟩ as x-axis and ratio N_G/N as y-axis. 

## Project Round 2
#### Problem Statement 1:
Using the dataset that you had selected for the first round create a network (for example, if the network is not already there as a dataset then if it is a social media twitter data create the follower/following graph/reply/retweet networks). Once you get the network do the following:

a) Find the giant component G in the network (note that giant components are the largest connected subgraph of the constricted network/graph). Let N_G denote the number of nodes in G. Find N_G/N where N is the total number of nodes in the network. 

b)Apply Girvan Newman algorithm and Ravasaz algorithm to find the communities step by step and illustrate each step the communities got and stop after 5 steps
Show all the communities and give your understanding about the communities that you got through the algorithm. All these things should be reported in the report that you are going to submit. Looking at the output given by the two algorithms compare and contrast the two algorithms.

#### Problem Statement 2:
a) Create a scale-free network using appropriate Python package (find out!). 
b)Apply ICM (Independent Cascade Model) to find the maximum number steps required to get to the maximum number of nodes. This you may repeat 5 times by starting from different nodes and see how many steps are required for the above. Activation probabilities for the pair of nodes which is needed for ICM can be assigned randomly. When you are assigning it randomly note this point: from a node say v if there are three edges to different vertices w,x, and y. Then it should be p(v,w)+p(v,x)+p(v,y)=1.

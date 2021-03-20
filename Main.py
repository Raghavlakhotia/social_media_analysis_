#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries 

# In[29]:


import networkx as nx
import matplotlib.pyplot as plt


# # Importing Dataset

# In[30]:


G1 =nx.read_edgelist("social_facebook_dataset.txt", create_using = nx.Graph(), nodetype=int)
G2 =nx.read_edgelist("Wiki-Vote.txt", create_using = nx.Graph(), nodetype=int)


# # Graph Information and Plotting 

# In[31]:


# Infomatio About the Graph
print(nx.info(G1))
print(nx.info(G2))


# In[32]:


#Plotting Graph : Social Facebook Network 
nx.draw(G1)


# In[33]:


#Plotting Graph : Wikipedia Network
nx.draw(G2)


# # Problem Statement 1: 
# # Centralities, Clustering Coefficient, Reciprocity and Transitivity

# ## 1. Degree Centrality

# In[34]:


def degreeCentrality(G):
    pos = nx.spring_layout(G)
    degCent = nx.degree_centrality(G)
    node_color = [20000.0 * G.degree(v) for v in G]
    node_size =  [v * 10000 for v in degCent.values()]
    plt.figure(figsize=(15,15))
    nx.draw_networkx(G, pos=pos, with_labels=False,
                     node_color=node_color,
                     node_size=node_size )
    plt.axis('off')
    #Printing Top 10 Nodes as per Degree Centrality
    print("Printing Top 10 Nodes as per Degree Centrality")
    sorted_degree=sorted(degCent, key=degCent.get, reverse=True)[:10]
    for d in sorted_degree[:10]:
        print("Node Label: ",d,"=>",G.degree[d])
        
#Facebook Network Centality
print("Facebook Network Degree Centality:\n")
degreeCentrality(G1)
# Wikipedia Network Degree Centality
print("\nWikipedia Network Degree Centality:\n")
degreeCentrality(G2)


# ## 2. Eigenvector Centrality

# In[51]:


def eigenVectorCentrality(G):
    pos = nx.spring_layout(G1)
    eigCent = nx.eigenvector_centrality(G1)
    node_color = [20000.0 * G1.degree(v) for v in G1]
    node_size =  [v * 10000 for v in eigCent.values()]
    plt.figure(figsize=(15,15))
    nx.draw_networkx(G1, pos=pos, with_labels=False,
                     node_color=node_color,
                     node_size=node_size )
    plt.axis('off')
    print("Printing Top 10 Nodes as per Eigenvector Centrality")
    sorted_degree=sorted(eigCent, key=eigCent.get, reverse=True)[:10]
    for d in sorted_degree[:10]:
        print("Node Label: ",d,"=>",G1.degree[d])
        
#Facebook Network Eigenvector Centality
print("Facebook Network Eigenvector Centality:\n")
eigenVectorCentrality(G1)
# Wikipedia Network Eigenvector Centality
print("\nWikipedia Network Eigenvector Centality:\n")
eigenVectorCentrality(G2)


# ## 3. Katz Centrality

# In[46]:


def katzCentrality(G):
    pos = nx.spring_layout(G)
    katzCent = nx.katz_centrality(G)
    node_color = [20000.0 * G.degree(v) for v in G]
    node_size =  [v * 10000 for v in katzCent.values()]
    plt.figure(figsize=(15,15))
    nx.draw_networkx(G, pos=pos, with_labels=False,
                     node_color=node_color,
                     node_size=node_size )
    plt.axis('off')
    #Printing Top 10 Nodes as per Eigenvector Centrality
    sorted_degree=sorted(katzCent, key=katzCent.get, reverse=True)[:10]
    for d in sorted_degree[:10]:
        print("Node Label: ",d,"=>",G.degree[d])
#Facebook Network Katz Centality
print("Facebook Network Katz Centality:\n")
katzCentrality(G1)
# Wikipedia Network Katz Centality
print("\nWikipedia Network Katz Centality:\n")
katzCentrality(G2)         


# ## 4. Pagerank

# In[45]:


def pagerankCentrality(G):
    pos = nx.spring_layout(G)
    pr = nx.pagerank(G, alpha = 0.8) 
    node_color = [20000.0 * G.degree(v) for v in G]
    node_size =  [v * 10000 for v in pr.values()]
    plt.figure(figsize=(15,15))
    nx.draw_networkx(G, pos=pos, with_labels=False,
                     node_color=node_color,
                     node_size=node_size )
    plt.axis('off')
    #Printing Top 10 Nodes as per Eigenvector Centrality
    sorted_degree=sorted(pr, key=pr.get, reverse=True)[:10]
    for d in sorted_degree[:10]:
        print("Node Label: ",d,"=> Degree: ",G.degree[d])
#Facebook Network Pagerank Centality
print("Facebook Network Pagerank Centality:\n")
pagerankCentrality(G1)
# Wikipedia Network Pagerank Centality
print("\nWikipedia Network Pagerank Centality:\n")
pagerankCentrality(G2) 


# ## 5. Betweeness Centrality

# In[48]:


def betweenessCentrality(G):
    pos = nx.spring_layout(G)
    betCent = nx.betweenness_centrality(G)
    node_color = [20000.0 * G.degree(v) for v in G]
    node_size =  [v * 10000 for v in betCent.values()]
    plt.figure(figsize=(20,20))
    nx.draw_networkx(G, pos=pos, with_labels=False,
                     node_color=node_color,
                     node_size=node_size )
    plt.axis('off')
    #Printing Top 10 Nodes as per Betweeness Centrality
    sorted_degree=sorted(betCent, key=betCent.get, reverse=True)[:10]
    for d in sorted_degree[:10]:
        print("Node Label: ",d,"=> Degree: ",G.degree[d])
#Facebook Network Betweeness Centality
print("Facebook Network Betweeness Centality:\n")
betweenessCentrality(G1)
# Wikipedia Network Betweeness Centality
print("\nWikipedia Network Betweeness Centality:\n")
betweenessCentrality(G2) 


# ## 6. Closeness Centrality

# In[52]:


def closenessCentrality(G):
    pos = nx.spring_layout(G)
    cloCent = nx.closeness_centrality(G)
    node_color = [20000.0 * G.degree(v) for v in G]
    node_size =  [v * 10000 for v in cloCent.values()]
    plt.figure(figsize=(13,13))
    nx.draw_networkx(G, pos=pos, with_labels=False,
                     node_color=node_color,
                     node_size=node_size )
    plt.axis('off')
    #Printing Top 10 Nodes as per Closeness Centrality
    sorted_degree=sorted(cloCent, key=cloCent.get, reverse=True)[:10]
    for d in sorted_degree[:10]:
        print("Node Label: ",d,"=> Degree: ",G.degree[d])
#Facebook Network Closeness Centality
print("Facebook Network Closeness Centality:\n")
closenessCentrality(G1)
# Wikipedia Network Closeness Centality
print("\nWikipedia Network Closeness Centality:\n")
closenessCentrality(G2) 


# ## 7. Group Betweenness Centrality

# In[44]:


def groupBetweenCentrality(G):
    pos = nx.spring_layout(G)
    gbCent = nx.group_betweenness_centrality(G)
    node_color = [20000.0 * G.degree(v) for v in G]
    node_size =  [v * 10000 for v in gbCent.values()]
    plt.figure(figsize=(13,13))
    nx.draw_networkx(G1, pos=pos, with_labels=False,
                     node_color=node_color,
                     node_size=node_size )
    plt.axis('off')
    #Printing Top 10 Nodes as per Closeness Centrality
    sorted_degree=sorted(gbCent, key=gbCent.get, reverse=True)[:10]
    for d in sorted_degree[:10]:
        print("Node Label: ",d,"=> Degree: ",G.degree[d])
    
#Facebook Network Group Betweeeness Centality
print("Facebook Network Group Betweeeness Centality:\n")
groupBetweenCentrality(G1)
# Wikipedia Network Group Betweeeness Centality
print("\nWikipedia Network Group Betweeeness Centality:\n")
groupBetweenCentrality(G2)     


# ## 1.2 Clustering Coefficient
# #### a) Local Clustering Coefficient
# #### b) Global Clustering Coefficient
# #### c) Average Clustering Coefficient

# In[ ]:


all_nodes = list(G1.nodes())
for node in all_nodes:
    local_clustering_coefficient=nx.clustering(G1,node)
    global_clustering_coefficient=(3*nx.triangles(G1,node))/nx.transitivity(G1)
    print("Local Clustering Coefficient of ",node," = ",local_clustering_coefficient)
    print("Global Clustering Coefficient of ",node," = ",global_clustering_coefficient)


# In[38]:


print("No. Of Nodes of Facebook Social Graph:",G1.number_of_nodes())
print("No. Of Edges of Facebook Social Graph",G1.number_of_edges())
print("No. Of Nodes of Wikipedia Network Graph:",G2.number_of_nodes())
print("No. Of Edges of Wikipedia Network Graph:",G2.number_of_edges())

# Average Clustering Coefficient
average_clustering_coefficient_G1=nx.average_clustering(G1)
average_clustering_coefficient_G2=nx.average_clustering(G2)
print("Average Clustering Coefficient of Facebook Social Graph: ", average_clustering_coefficient_G1)
print("Average Clustering Coefficient of Wikipedia Network Graph: ", average_clustering_coefficient_G2)


# ## 1.3 Reciprocity

# In[53]:


print("Reciprocity of Facebook Social Graph is: ",nx.overall_reciprocity(G1))
print("Reciprocity of Wikipedia Vote Network Graph is: ",nx.overall_reciprocity(G2))


# ## 1.4 Transitivity

# In[40]:


print("Transitivity of Facebook Social Graph is: ",nx.transitivity(G1))
print("Transitivity of Wikipedia Vote Network Graph is: ",nx.transitivity(G2))


# # Problem Statement 2: Giant component variation 

# In[41]:


giant_facebook = len(max(nx.connected_components(G1), key=len))
print("Number of node in the Giant Componenet of G ="+str(giant_facebook)+'\n')
giant_wiki = len(max(nx.connected_components(G2), key=len))
print("Number of node in the Giant Componenet of G ="+str(giant_wiki)+'\n')


# In[ ]:


# Importing required libraries
import networkx as nx
import matplotlib.pyplot as plt
import pylab as plt

n = 500
arr = {} # Dictionary to store k and corresponding Ng/N value
for i in range(0,51):
    k = float(i/10) # k varies by 0.1
    p = k/(n-1)
    g = nx.erdos_renyi_graph(n, p)
    # finding Giant component and ng
    giant = max(nx.connected_components(g), key=len)
#     ng = giant_components(giant)
    ng = len(giant)
    # adding the ratio to dictionary
    arr[k] = float(ng/n)
# since dictionary is unsorted collection, sorting wrt k for plotting
temp = sorted(arr.items())
# unzipping keys and values of dictionary into x and y
# x takes the value of k , y takes the ratio in sorted order
x,y = zip(*temp)

# plotting the histogram
plt.figure()
plt.grid(True)
plt.plot(x,y)
plt.title('Ng/N variation with k')
plt.xlabel( 'k' )
plt.ylabel( 'Ng/N' )
plt.show()
plt.close()


# In[ ]:






from collections import deque

queue = deque

def enqueue(q, item):
    q.append(item)

def dequeue(q):
    return q.popleft()

# defining and returning the dictionary representing a graph
def exampledict():    
    adj = dict()
    adj['r'] = ['s', 'v']
    adj['s'] = ['w', 'r']
    adj['t'] = ['u', 'w', 'x']
    adj['u'] = ['t', 'x', 'y']
    adj['v'] = ['r']
    adj['w'] = ['s', 't', 'x']
    adj['x'] = ['t', 'u', 'w', 'y']
    adj['y'] = ['u', 'x']
    return adj

l = []

# reading the 'graphdata.txt' file 
with open("Q:\My Drive\Study\Courses\CE537\Assignments\A7\graphdata.txt", "r") as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split()]
        l.append(inner_list)

# requires: a list format of the graph
# returns: a dictionary format of the UNDIRECTED graph
def read_list(l):
    if len(l[0])==1:
        l=l[1:]
    else:
        l = l
    adj = dict()
    x = helper1(l)
    temp = helper1(l)
    adj = helper2(x,adj)
    adj = helper3(temp,adj)  # use only if the graph is undirected
    return adj


# requires: a list format of the graph
# returns: a list containing 2 sub-lists (first elements and second elements)
def helper1(l):
    i = 0
    x1=[]
    x2=[]
    while i<len(l):
        x = l[i]
        x1.append(x[0])  # contains all first elements of the list
        x2.append(x[1])  # contains all second elements of the list
        i = i + 1
    return [x1,x2]

# requires: a list representing a graph and an empty dictionary
# returns: dictionary representing the graph in a directed format
def helper2(x,adj):
    x1 = x[0]           # contains all first elements of the list
    x2 = x[1]           # contains all second elements of the list
    i=0
    while i<len(x1):
        y1 = x1[i]  # first elements will be the keys in the adj dict
        slist=[]
        if y1!='null':  # key not seen yet
            slist.append(x2[i])  
            for j in range(i+1,len(x1)): # if other same value keys exist
                if x1[j]==y1:
                    slist.append(x2[j])
                    x1[j]='null'        # mark them seen as null
            adj[y1]=slist
            i=i+1 
        else:          # key seen already
            i=i+1    
    return adj

# requires: a list representing a graph and a dictionary 
#           representing the graph in a directed format
# returns: dictionary representing the graph in an undirected format
def helper3(temp,adj):
    z1 = temp[1]       # contains all second elements of the list
    z2 = temp[0]       # contains all first elements of the list
    # terminilogy is swapped above, if compared to "helper2"
    i=0
    while i<len(z1):
        y1 = z1[i]     # second elements will be the keys in the adj dict
        if y1!='null': # key not seen yet in helper3 code
            flag=0
            for key in adj:  # checking if key already exists from helper2
                if y1==key:
                    flag=1                 
            if flag==1:     # key already exists from helper2
                slist1 = adj[y1]  # importing corresponding list
                k=0; count=0
                while k<len(slist1):  # check is list already contains z2[i]
                    if slist1[k]==z2[i]: 
                        count = 1     # list contains z2[i] - skip procedure
                    k=k+1          
                if count==0:  # list does not contain z2[i]
                    slist1.append(z2[i])
                for j in range(i+1,len(z1)): # if other same value keys exist
                    if z1[j]==y1:
                        k=0; count=0
                        while k<len(slist1): # check is list already contains z2[i]
                            if slist1[k]==z2[j]:
                                count = 1    # list contains z2[i] - skip procedure
                            k=k+1       
                        if count==0:   # list does not contain z2[i]
                            slist1.append(z2[j])
                            z1[j]='null'     # mark them seen as null
                adj[y1]=slist1
            else:           # key does not exist from helper2
                slist=[]    # creating new corresponding list
                slist.append(z2[i])
                for j in range(i+1,len(z1)): # if other same value keys exist
                    if z1[j]==y1:
                        slist.append(z2[j])
                        z1[j]='null'         # mark them seen as null
                adj[y1]=slist
            i=i+1 
        else:      # key seen already
            i=i+1            
    return adj

# code provided by Dr. Baugh for BFS (breadth first search) implementation
# requires: adj as the graph and s as the starting node
# returns: distance dictionary 'd' - distance from source for each node
#          predecessor dictionary 'pi' - predecessor for each node
def bfs(adj, s): 
    color = dict()
    d = dict()
    pi = dict()
    for u in adj.keys():
        color[u] = 'white'     # color of vertex 'u'
        d[u] = float('inf')    # distance of source 's' to vertex 'u'
        pi[u] = None           # predecessor of vertex 'u'
    color[s] = 'gray'          # initializing the source 's' as gray
    d[s] = 0                   # distance of source to source = 0
    pi[s] = None               # predecessor of sourse 's' is NONE
    q = queue()                # initializing a queue (FIFO)
    enqueue(q, s)              # adding source 's' to the queue
    while len(q) != 0:
        print('q =', q)
        u = dequeue(q)         # FIFO queue
        for v in adj[u]:
            if color[v] == 'white':   # unseen node
                color[v] = 'gray'     # marking node as seen
                d[v] = d[u] + 1       # distance increment
                pi[v] = u             # storing predecessor node
                enqueue(q, v)         # adding node to the queue
        color[u] = 'black'            # not essentially required
    return d, pi

# DFS - depth first search code - uses list (as a STACK)
# requires: adj as the graph and s as the starting node
# returns: distance dictionary 'd' - distance from source for each node
#          predecessor dictionary 'pi' - predecessor for each node
# 'd' and 'pi' depend on how the 'dfs' function traverses the graph
def dfs(adj, s): 
    color = dict()
    d = dict()
    pi = dict()
    for u in adj.keys():
        color[u] = 'white'     # color of vertex 'u'
        d[u] = float('inf')    # distance of source 's' to vertex 'u'
        pi[u] = None           # predecessor of vertex 'u'
    color[s] = 'gray'          # initializing the source 's' as gray
    d[s] = 0                   # distance of source to source = 0
    pi[s] = None               # predecessor of sourse 's' is NONE
    q = []                     # initializing a list as a stack (LIFO)
    q.append(s)                # adding source 's' to the list
    while len(q) != 0:
        print('q =', q)
        u = q.pop()            # LIFO list
        for v in adj[u]:
            if color[v] == 'white':    # unseen node
                color[v] = 'gray'      # marking node as seen
                d[v] = d[u] + 1        # distance increment
                pi[v] = u              # storing predecessor node
                q.append(v)            # adding node to the list
        color[u] = 'black'             # not essentially required
    return d, pi   

# Testing the code

# Problem 1:
#adj = exampledict()              # use if testing with Dr. Baugh's graph
adj = read_list(l)
print(adj)

# Problem 2 and 3:
d, pi = bfs(adj, '1')              # BFS implementation
#d, pi = dfs(adj, '1')               # DFS implementation

for u in adj.keys():
    print(u, pi[u], d[u])

# requires: source and ending nodes for the required path
# returns: the shortest path if using BFS
#          a path (not necessarily the shortest) if using DFS
def print_path(adj, s, v):
    if v == s:
        print(s)
    elif pi[v] == None:
        print('no path')
    else:
        print_path(adj, s, pi[v])
        print(v)

# printing the paths
print_path(adj,'1','12')
print_path(adj,'1','8')
print_path(adj,'1','4')
print_path(adj,'1','10')

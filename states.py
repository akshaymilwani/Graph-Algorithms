
from collections import deque
import copy

queue = deque

def enqueue(q, item):
    q.append(item)

def dequeue(q):
    return q.popleft()

# requires: a state in the graph (assumed as the source state in this method)
# returns: all adjacent 'legal' states stemming from the source state
# assumption: need to change value of n (no. of locations - p,q,r)
def adj_states(s):
    adjss = []
    n = 3 # no. of locations
    for count in range(0,n):
        alo = []
        print(alo)
        for i in range(0,n):
            alo.append(copy.deepcopy(s[i]))
        if len(alo[count])>=1:   
            temp = alo[count].pop()
            for j in range(0,n):
                alob = []
                temp2=copy.deepcopy(alo)
                if j==count:
                    continue
                else:
                    temp2[j].append(temp)  
                for k in range(0,n):
                    alob.append(temp2[k])
                adjss.append(alob)   
    return adjss 

# BFS - breadth first search code - uses queue
# requires: starting and ending states of a graph
# returns: distance dictionary 'd' - distance from source state for each state
#          predecessor dictionary 'pi' - predecessor for each state
#          list 'count' - of all unique states created
def bfs(ss,sg): 
    color = dict()
    d = dict()
    pi = dict()
    count = [0]                      # initializing count[0] as 0
    count.append(ss)                 # each state has a unique identification number = count.index(state)
    color[count.index(ss)] = 'gray'  # initializing the source state 'ss' as gray
    d[count.index(ss)] = 0           # distance of source to source = 0
    pi[count.index(ss)] = None       # predecessor of sourse 'ss' is NONE
    q = queue()                      # initializing a queue (FIFO)
    enqueue(q,ss)                    # adding source 'ss' to the queue
    while len(q) != 0:
        print('q =', q)
        u = dequeue(q)               # FIFO queue
        adj = adj_states(u)          # get adjacent states
        for i in range(0,len(adj)):  # traverse through all adjacent states acquired
            snew = adj[i]            # an adjacent state
            flag=0
            for j in range(0,len(count)): 
                if snew==count[j]:
                    flag=1
            if flag==0:                  # state has not been marked yet
                count.append(snew)       # mark the state as gray and append to list 'count'
                color[count.index(snew)] = 'gray'                    
                pi[count.index(snew)] = u
                d[count.index(snew)] = d[count.index(u)] + 1
                enqueue(q, snew)         # adding node to the queue
        color[count.index(u)] = 'black'  # not essentially required     
    return d, pi, count

# DFS - depth first search code - uses list (as a STACK)
# requires: starting and ending states of a graph
# returns: distance dictionary 'd' - distance from source state for each state
#          predecessor dictionary 'pi' - predecessor for each state
#          list 'count' - of all unique states created
# 'd' and 'pi' depend on how the 'dfs' function creates the graph
def dfs(ss,sg): 
    color = dict()
    d = dict()
    pi = dict()
    count = [0]                        # initializing count[0] as 0
    count.append(ss)                   # each state has a unique identification number = count.index(state)
    color[count.index(ss)] = 'gray'    # initializing the source state 'ss' as gray
    d[count.index(ss)] = 0             # distance of source to source = 0
    pi[count.index(ss)] = None         # predecessor of sourse 'ss' is NONE
    q = []                             # initializing a list as a stack (LIFO)
    q.append(ss)                       # adding source 'ss' to the list
    while len(q) != 0:
        print('q =', q)
        u = q.pop()                    # LIFO list        
        adj = adj_states(u)            # get adjacent states
        for i in range(0,len(adj)):    # traverse through all adjacent states acquired
            snew = adj[i]              # an adjacent state
            flag=0
            for j in range(0,len(count)):
                if snew==count[j]:
                    flag=1
            if flag==0:                  # state has not been marked yet
                count.append(snew)       # mark the state as gray and append to list 'count'    
                color[count.index(snew)] = 'gray'                    
                pi[count.index(snew)] = u
                d[count.index(snew)] = d[count.index(u)] + 1
                q.append(snew)           # adding node to the list
        color[count.index(u)] = 'black'  # not essentially required       
    return d, pi, count    

# Testing the code

# Problem 4 and 5:
ss=[['b','a'],[],[]]            # 2 blocks A,B
sg = [[],['b','a'],[]]
#ss=[['b','a','c'],[],[]]       # 3 blocks A,B,C
#sg = [['b','c'],['a'],[]]
#ss=[['b','a','c','d'],[],[]]   # 4 blocks A,B,C,D
#sg = [['b','c'],['a'],['d']]
d, pi, count = bfs(ss,sg)       # BFS implementation
#d, pi, count = dfs(ss,sg)      # DFS implementation
m = len(d)                      # number of states generated
print('no. of states generated =',m)    

for k in range(2,len(count)):
    print(k,count.index(pi[k]), d[k])

# requires: starting and ending states for the required path
# returns: a path shown as different states
#          the shortest path if using BFS
#          a path (not necessarily the shortest) if using DFS
def print_path(ss,sg):
    if ss == sg:
        print(ss)
    elif pi[count.index(sg)] == None:
        print('no path')
    else:
        print_path(ss,pi[count.index(sg)])
        print(sg)
     
# printing the paths
print_path(ss,sg)
print_path([['b', 'a'], [], []],[[],['a','b'],[]])





#!/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:27:36 2017

@author: bhupeshgupta
"""

'''
Solution Balanced forest. 

Solution Steps 
1) Input coins coins_list - [0,C1,C2,...],edges (X,Y) in Node_Dict - {NODE:[Connected Nodes]}
2) Next traverse tree depth first and Save Score, time_in, time_out in a Tree_Dict
Tree_Dict - {Node: {'score':Si ,'in':in_time, 'out': out_time}}
3) Next we segregate nodes with similar score into Min_time Or Max_time DICT based on time of entry
4) Once we have this we can go about finding Cmin by checking each node. 

So the idea is that we check each node using the score for that node. As we are doing an exhaustive search
we are sure that we will land on a node which will represent atleast 1 actual C2 and 1 actual C3 or C3+C2 for sure.
We may be lucky to get a node which has similar score as C2 or C3 and may not be actual one but that is a False positive. 
so for a particular node with score of C3 or C2, we check if it is valid and if yes then get Cmin. 
We keep doing this with each node. so that we get the minimun Cmin. 
if not then we get -1. 

Now lets check the cases 

Checks for each node. for a given Node n
we can have following cases 
Case1: Score n == 0 i.e. add an extrenal node with Score = sum/2 this is maximum Cmin you can get. 
Case2: Score n > 0 and < Sum/3 that means Score may be equal to C3. for this check SUBCASES2
Case3: Score n > sum/3 and <= sum/2 this may be representing a possible C2. check SUBCASES3
Case4: Score n > Sum/2, does not represent any useful infomration hence discard. We have reduced half of the nodes. 

for case2 we can have following SUBCASES 
SUBCASE2.1 - C3 in Leaf Tree -> if this node represents a C3 in a leaf tree then we should check 
that a corresponding node C2 exist which has score (SUM-ScoreN)//2 and does not encapsulated C3. 
We can check this by checking that either C2 entry after C3 entry becasue C3 cannot enclose a C2 
or C2 Exit before equal C3 Entry 
SubCase2.2 -> C3 in internal Tree -> In such a case we we will have C2+C3 combined as Score will be very high. 
hence we should check that we have a C2+C3 and also that C3 Included in C2. How de we check that. 
Check C2+C3 entry before C3 Entry and C2+C3 exit after or equal to C3 Exit

For Case3 we can have following SubCases 
SubCase3.1 - two distinct C2's: if we find 2 distinct C2's that case is a possible case
SubCase3.2 - Leaf Tree C3: Check that there exist a C3 and it is not enclosed in C2 
Subcase 3.3 - Internal Tree C3: Check C2+C3 exist if yes then thats a probable case 
SubCase3.4 - Adjacent C2's:  Check is 2*C2 available, if yes then that is a possible case 

for each of these check Cw which is (3*C2 - Sum)

Finally after checking all these cases is we get Cmin != None then answer else -1
Cool this looks like a solution. Lets implement this now
'''
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__ , (time2-time1)*1000.0))
        return ret
    return wrap



# required Methods 
#@timing
def depth_first_traversal(node, prev_node):
    '''
    This is an improtant function and has recurssion, so this may fail. we will make this and then optimize. 
    for a given Node and Prev_node, we need to create tree_dict with score, in_time and out_time
    
    lets write pseudocode for it and then implement it
    '''    
    # Score equal to sum of coins in each connected nodes + coin in node 
    # We start the ticker with 1 and it increases each time we call the function
    global ticker    
    ticker += 1
    # for a given node save in time = ticker and score = coins in the node
    tree_dict[node]['in'] = ticker
    tree_dict[node]['score'] = coins_list[node]
    # now lets calculate the score for the node
    # run a for loop on each child node (except the prev_node)
    for child in node_dict[node]:
        if child != prev_node:
    # go for depth of connected node if it has any node other than prev this will store the score for connected node
            depth_first_traversal(child, node)
    # save the score of node = score + score_connected_node
            tree_dict[node]['score'] += tree_dict[child]['score']
    # while exiting the loop save exit time 
    tree_dict[node]['out'] = ticker
    # return none
    return 

def valid_C3(node):
    '''
    to check valid_c3 we check following subcases here 
    1) Leaf tree - that means C3 tree is in one corner. lets say the node we are inspecting represents 
        valid_C3 and is either on left or right leaf then for such a node we should have a valid C2 and 
        also that C2 should not overlap with this C3. 
    2) Internal SubTree - 
    '''
    global Cmin
    C3 = tree_dict[node]['score']
    # Find Score C2 for given 
    C2 = (tree_sum - C3)//2
    Cw = C2-C3
    if ((tree_sum - C3)%2 != 0):
        return
    # leaf Tree
    # first if will check if C2 in max and (C2 entry after C3 entry(i.e. c2 not contained) or C2 exit before C3 entry (obviously not contained)
    # second if will check if C2 in min and (C2 entry after C3 entry(i.e. c2 not contained) or C2 exit before C3 entry (obviously not contained)
    if (C2 in max_time.keys()) and ((tree_dict[max_node[C2]]['in'] > tree_dict[node]['in']) or (tree_dict[max_node[C2]]['out'] < tree_dict[node]['in'])):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)
    elif (C2 in min_time.keys()) and ((tree_dict[min_node[C2]]['in'] > tree_dict[node]['in']) or (tree_dict[min_node[C2]]['out'] < tree_dict[node]['in'])):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)    
    
    # Internal SubTree
    # if C2+C3 exist and C3 is contained in it, that means C2+C3 entry before C3 Entry and C2+C3 exit after or equal to C3 entry)
    elif ((C2+C3) in min_time.keys()) and ((tree_dict[min_node[C2+C3]]['in'] < tree_dict[node]['in']) and (tree_dict[min_node[C2+C3]]['out'] >= tree_dict[node]['in'])):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)
    elif ((C2+C3) in max_time.keys()) and ((tree_dict[max_node[C2+C3]]['in'] < tree_dict[node]['in']) and (tree_dict[max_node[C2+C3]]['out'] >= tree_dict[node]['in'])):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)
    return 


def valid_C2(node):
    '''
    this is to validate various cases if Score > Sum/3 and < sum/2 the cases are 
    1) 2 distinct C2 if we get awesome 
    2) C3 is a leaf tree
    3) C2+C3 exist 
    4) 2 adjacent C2 exist 
    '''
    # Variables needed 
    global Cmin
    C2 = tree_dict[node]['score']
    # get C3 and Cw for the C2
    Cw = 3*C2 - tree_sum
    C3 = C2-Cw
    # if 2 distinct C2's 
    if (min_time[C2] != max_time[C2]):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)
    
    # if C3 exist and not enclosed in C2 
    elif (C3 in max_time.keys()) and ((tree_dict[node]['in'] > tree_dict[max_node[C3]]['in']) or (tree_dict[node]['out'] < tree_dict[max_node[C3]]['in'])):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)
    elif (C3 in min_time.keys()) and ((tree_dict[node]['in'] > tree_dict[min_node[C3]]['in']) or (tree_dict[node]['out'] < tree_dict[min_node[C3]]['in'])):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)
        
    # C2+ C3 Exist
    elif ((C2+C3) in min_time.keys()):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)
        
    # 2*C2 exist
    elif ((2*C2) in min_time.keys()):
        Cmin = Cw if Cmin == None else min(Cmin, Cw)
    return

#@timing
# main function 
def main():
    # get number of nodes in a tree and 
    N = int(input())
    # define global variables we need such as Coins_list, Node_Dict, Tree_Dict, Min_Time, Max_Time etc 
    global coins_list, node_dict, tree_dict, min_time, max_time, min_node, max_node, ticker, Cmin, tree_sum
    node_dict = {i:[] for i in range(1, N+1)} # this will contain edges, i.e. connected nodes for each node
    tree_dict = {i: {'score':0, 'in': 0, 'out':0} for i in range(1,N+1)}
    min_time, max_time, min_node, max_node = {}, {}, {}, {} # store {score:in_time} and {score:node}
    ticker, tree_sum = 0,0
    Cmin = None
     
    # get inputs from user i.e. Coins and Edges and store them
    coins_list = [0] + [x for x in list(map(int, input().split()))] # coins_list
    tree_sum = sum(coins_list)
    for _ in range(1,N):
        x,y = map(int, input().split())
        node_dict[x].append(y)
        node_dict[y].append(x)
    # DEBUGGING PRINT STATEMENT
#    print(N, coins_list, tree_sum, node_dict)
    # create tree_dict using depth_first traversal store, score, in_time, out time
    depth_first_traversal(1,0)
    # DEBUGGING PRINT STATEMENT
#    print(tree_dict)
    # using tree_dict segregate nodes in min_time and max_time dict which has time against score
    for node in range(1, N+1):
        # if node is not present add it in min_time and max_time
        if (tree_dict[node]['score'] not in min_time.keys()): 
            min_time[tree_dict[node]['score']] = tree_dict[node]['in']
            min_node[tree_dict[node]['score']] = node
            max_time[tree_dict[node]['score']] = tree_dict[node]['in']
            max_node[tree_dict[node]['score']] = node
        # else if in time of node greater that min_time put it in max 
        elif (tree_dict[node]['in'] > min_time[tree_dict[node]['score']]):
            max_time[tree_dict[node]['score']] = tree_dict[node]['in']
            max_time[tree_dict[node]['score']] = node
        # else just edit the min_time dict with the node in time and node because we can have only 2 timings for a similar score no other cases
        else:
            min_time[tree_dict[node]['score']] = tree_dict[node]['in']
            min_time[tree_dict[node]['score']] = node
    # DEBUGGING PRINT STATEMENT
#    print(min_time, min_node, max_time, max_node)        
            
    # check for special case i.e. C2 == tree_sum/2 if yes, then save Cmin as tree_sum/2
    if (tree_sum%2 == 0) and (tree_sum//2 in min_time.keys()):
        Cmin = tree_sum//2
    # run for loop over each node and 
    for node in range(1, N+1):
    # if score > 0 and < sum/3 check valid_C3 and get Cmin for valid cases
        if (tree_dict[node]['score'] <= tree_sum//3):
            valid_C3(node)
    # else if score >= sum/3 and < sum/2 check valid_C2. and get Cmin for valid cases
        elif (tree_dict[node]['score'] <= tree_sum//2): 
            valid_C2(node)
    # finally if Cmin is None, print -1 else print Cmin
    
    if (Cmin == None):
        print(-1)
    else:
        print(Cmin)
        
    return 



if __name__ == '__main__':
    T = int(input()) # number of trees as inputs
    for _ in range(T):
        main()




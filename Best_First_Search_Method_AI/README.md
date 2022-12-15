A.1 Aim: 
To find shortest path from the starting node to a goal node using Best First search algorithm with Python.

A.2Prerequisite: Basic understanding of search algorithms.

A.3 Learning Outcome:
After completing this experiment, you will be able to
1. Understand Significance of Heuristic function
2. Implement Best First Search Algorithm to find the shortest path

A.4 Theory:

A.4.1 Heuristic function
A heuristic in the most common sense is a method involving adapting the approach to a 
problem based on previous solutions to similar problems. Approaches aim to be easily and 
quickly applicable to a range of problems.
Basic idea of heuristic search is- Rather than trying all possible search paths at each step, try 
to find which paths seem to be getting us nearer to our goal state.
Heuristic function is used in informed search to find the most promising path. It takes current 
state of the agent as input and finds how close the agent is from the goal state. Does not always 
give the best solution, but finds a good solution in a reasonable time. It is represented by ℎ(𝑛).


A.4.2 Best First Search Algorithm
Steps
 1. Start with OPEN list (Prioritized list) containing just initial state.
 2. Create a list called CLOSED (Visited list) i.e., initially empty. 
 3. If the OPEN list is empty search ends unsuccessfully. 
 4. Remove the first node on OPEN list and put this node on CLOSED list. 
 5. If this is a goal node, search ends successfully. 
 6. Generate successors of this node: 
 For each successor :
◼ (a). If it has not been discovered / generated before i.e., it is not on OPEN, 
evaluate this node by applying the heuristic function, add it to the OPEN 
and record its parent
◼ (b). If it has been discovered / generated before, change the parent if the 
new path is better than the previous one
◼ In that case update the cost of getting to this node and to any successors 
that this node may already have
 7. Reorder the list OPEN, according to the heuristic merit
 8. Go to step 3


A.4.3 Example- Travel from “a” to “z”
Here the number on the edges represent distance from one node to another. And number written 
on each node is distance of the node from the goal node.





Steps for implementing above problem-Here start node is A and current node is Z
Start node: A
Open: (A,21)
Close: ()
Explore current node A
Check if current node A= Goal node Z
Open: (B,14), (C,18), (D,18)
Close: (A,21)
Current node= minDist(B,C,D)= B
Explore current node B
Check if current node B= Goal node Z
Open: (E,5), (C,18), (D,18)
Close: (A,21), (B,14)
Current node= minDist(E,C,D)=E
Explore current node E
Check if current node E= Goal node Z
Open: (Z,0), (C,18), (D,18)
Close: (A,21), (B,14),(E,5)
Current node= minDist(Z,C,D)=Z
Explore current node Z
Check if current node Z= Goal node Z
Open: (C,18), (D,18)
Close: (A,21), (B,14), (E,5), (Z,0)

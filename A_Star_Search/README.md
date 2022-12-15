A.1 Aim: 
a. To implement A* algorithm for the given graph problem
b. Compare the results with best first search algorithm output

A.2
Prerequisite: Basic understanding of search algorithms

A.3 Learning Outcome:
After completing this experiment, you will be able to:
1. Understand significance of Heuristic function
2. Implement A* algorithm to find the optimum path

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

A.4.2 A* Algorithm
It is the most common informed search algorithm. Uses the evaluation function

𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
 Where g(n) is the path cost from the initial state to node 
 h(n) is the estimated cost of the shortest path from to a goal state
 f(n) = estimated cost of the best path that continues from n to a goal.
Algorithm-
• The implementation of A* Algorithm involves maintaining two lists- OPEN and 
CLOSED

• OPEN contains those nodes that have been evaluated by the heuristic function but have 
not been expanded into successors yet.
• CLOSED contains those nodes that have already been visited.
Step-01:
• Define a list OPEN.
• Initially, OPEN consists solely of a single node, the start node S.
Step-02:
If the list is empty, return failure and exit.
Step-03:
• Remove node n with the smallest value of f(n) from OPEN and move it to list CLOSED.
If node n is a goal state, return success and exit.
Step-04:
Expand node n.
Step-05:
• If any successor to n is the goal node, return success and the solution by tracing the path 
from goal node to S.
• Otherwise, go to Step-06.
Step-06:
For each successor node,
• Apply the evaluation function f to the node.


• If the node has not been in either list, add it to OPEN.
Step-07:
Go back to Step-02.
A.4.3 Example- Travel from “a” to “z”
Here the number on the edges represent distance from one node to another. And number written 
on each node is distance of the node from the goal node.


![image](https://user-images.githubusercontent.com/57552973/207906432-79932d21-d7ca-434e-8a6a-e0cbc13ecd8f.png)



Write the steps for implementing above problem in your notebooks
Here start node is A and current node is Z

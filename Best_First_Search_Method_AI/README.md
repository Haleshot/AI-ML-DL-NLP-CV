# Best First Search Algorithm

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Learning Outcome](#learning-outcome)
- [Theory](#theory)
  - [Heuristic Function](#heuristic-function)
  - [Best First Search Algorithm](#best-first-search-algorithm)
  - [Example - Travel from "a" to "z"](#example-travel-from-a-to-z)

## Aim
The aim of this project is to find the shortest path from the starting node to a goal node using the Best First search algorithm implemented with Python.

## Prerequisite
Basic understanding of search algorithms is required to understand this project.

## Learning Outcome
After completing this experiment, you will be able to:
1. Understand the significance of the heuristic function in informed search.
2. Implement the Best First Search Algorithm to find the shortest path.

## Theory

### Heuristic Function
A heuristic function is a method that adapts the approach to a problem based on previous solutions to similar problems. In the context of search algorithms, a heuristic function helps in finding the most promising path by considering the current state of the agent and estimating how close it is to the goal state. It is denoted as ℎ(𝑛). The heuristic function does not always give the best solution but finds a good solution in a reasonable time.

### Best First Search Algorithm
The Best First search algorithm follows these steps:
1. Start with an OPEN list (prioritized list) containing just the initial state.
2. Create a list called CLOSED (visited list), initially empty.
3. If the OPEN list is empty, the search ends unsuccessfully.
4. Remove the first node from the OPEN list and put it on the CLOSED list.
5. If this node is a goal node, the search ends successfully.
6. Generate successors of the current node:
   - For each successor:
     - If it has not been discovered/generated before (i.e., not in the OPEN list), evaluate this node by applying the heuristic function, add it to the OPEN list, and record its parent.
     - If it has been discovered/generated before, change the parent if the new path is better than the previous one. Update the cost of getting to this node and to any successors that this node may already have.
7. Reorder the OPEN list according to the heuristic merit.
8. Go to step 3.

### Example - Travel from "a" to "z"
In this example, the graph represents a path from node "a" to node "z", where the numbers on the edges represent the distance between nodes and the numbers on each node represent the distance of the node from the goal node.

![Graph Travel Example](https://user-images.githubusercontent.com/57552973/207903823-cacbd80e-80fe-4ff8-b2a9-d269ab949a8a.png)

Steps for implementing the above problem:
- Start node: A
- OPEN: (A, 21)
- CLOSED: ()
- Explore current node A
- Check if current node A = Goal node Z
- OPEN: (B, 14), (C, 18), (D, 18)
- CLOSED: (A, 21)
- Current node = minDist(B, C, D) = B
- Explore current node B
- Check if current node B = Goal node Z
- OPEN: (E, 5), (C, 18), (D, 18)
- CLOSED: (A, 21), (B, 14)
- Current node = minDist(E, C, D) = E
- Explore current node E
- Check if current node E = Goal node Z
- OPEN: (Z, 0), (C, 18), (D, 18)
- CLOSED: (A, 21), (B, 14), (E, 5)
- Current node = minDist(Z, C, D) = Z
- Explore current node Z
- Check if current node Z = Goal node Z
- OPEN: (C, 18), (D, 18)
- CLOSED: (A, 21), (B, 14), (E, 5), (Z, 0)

## Output
Here are three screenshots showcasing the output obtained from running the Best First search algorithm.

![Screenshot 1](https://user-images.githubusercontent.com/57552973/207904053-77fda6a1-dd01-4a12-b9b0-ad12787d5c8d.png)

![Screenshot 3](https://user-images.githubusercontent.com/57552973/207904113-9eb58a08-d739-4bcc-8aeb-adc706c670e4.png)

![Screenshot 3](https://user-images.githubusercontent.com/57552973/207904240-56b9cd48-eb16-44b3-a718-d8500f53c202.png)

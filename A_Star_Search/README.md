# A* Algorithm Implementation

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Learning Outcome](#learning-outcome)
- [Theory](#theory)
  - [Heuristic function](#heuristic-function)
  - [A* Algorithm](#a-algorithm)
  - [Example - Travel from "a" to "z"](#example)

## Aim
The aim of this project is:
- To implement the A* algorithm for the given graph problem.
- To compare the results with the best-first search algorithm output.

## Prerequisite
Basic understanding of search algorithms is required to understand this project.

## Learning Outcome
After completing this experiment, you will be able to:
1. Understand the significance of the heuristic function in informed search.
2. Implement the A* algorithm to find the optimum path.

## Theory

### Heuristic function
A heuristic function is a method that adapts the approach to a problem based on previous solutions to similar problems. In the context of search algorithms, a heuristic function helps in finding the most promising path by considering the current state of the agent and estimating how close it is to the goal state. It is denoted as ℎ(𝑛). The heuristic function does not always give the best solution but finds a good solution in a reasonable time.

### A* Algorithm
The A* algorithm is the most common informed search algorithm. It uses an evaluation function, 𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛), to determine the best path to a goal state. Here:
- 𝑔(𝑛) is the path cost from the initial state to node 𝑛.
- ℎ(𝑛) is the estimated cost of the shortest path from node 𝑛 to a goal state.
- 𝑓(𝑛) is the estimated cost of the best path that continues from node 𝑛 to a goal.

The algorithm involves maintaining two lists: OPEN and CLOSED.
- OPEN contains nodes that have been evaluated by the heuristic function but have not been expanded into successors yet.
- CLOSED contains nodes that have already been visited.

The steps of the A* algorithm are as follows:
1. Initialize a list called OPEN with the start node.
2. If the list is empty, return failure.
3. Remove the node with the smallest value of f(n) from OPEN and move it to CLOSED. If the node is a goal state, return success.
4. Expand the selected node.
5. If any successor to the current node is the goal node, return success and the solution by tracing the path from the goal node to the start node.
6. For each successor node, apply the evaluation function f.
7. If the node has not been in either list, add it to OPEN.
8. Repeat from step 2.

### Example
The graph represents a path from node "a" to node "z", where the numbers on the edges represent the distance between nodes and the numbers on each node represent the distance of the node from the goal node.

![Graph Travel Example](https://user-images.githubusercontent.com/57552973/207906432-79932d21-d7ca-434e-8a6a-e0cbc13ecd8f.png)

### Output
![Output Screenshot](https://user-images.githubusercontent.com/57552973/207906767-a7c1624a-eebb-4424-835f-5ed7dd0448b8.png)

---

Feel free to check out the [repository](https://github.com/Haleshot/AI-ML/tree/master/A_Star_Search) for the code and more details.

This project was implemented using the following tools and libraries:
- [Python language](https://www.python.org/)

For more information, please refer to the repository linked above.

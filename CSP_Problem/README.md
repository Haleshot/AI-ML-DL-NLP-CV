# Constraint Satisfaction Problem (CSP)

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Learning Outcome](#learning-outcome)
- [Theory](#theory)
  - [Constraint Satisfaction Problem (CSP)](#constraint-satisfaction-problem-csp)
  - [Example](#example)
- [Task to be Completed](#task-to-be-completed)
- [Output](#output)

## Aim
The aim of this project is to implement a Constraint Satisfaction Problem (CSP) in Python for the following problem:
1. Find all (x, y) pairs where x ∈ {1, 2, 3} and 0 <= y < 10, and x + y >= 5.
2. Solve the 4-Queen problem and Sudoku.

## Prerequisite
Basic understanding of constraint satisfaction problem is required to understand this project.

## Learning Outcome
After completing this experiment, you will be able to:
1. Formulate a CSP.
2. Implement a small problem with constraints in Python.

## Theory

### Constraint Satisfaction Problem (CSP)
A Constraint Satisfaction Problem (CSP) can be defined by a set of three components: X, D, and C.
- X: Set of variables {X1, X2, ..., Xn}.
- D: Set of domains {D1, D2, ..., Dn} for each variable.
- C: Set of constraints that specify allowable combinations of values.

### Example
For example, if X1 and X2 have the same domain {1, 2, 3}, and the constraint states that X1 > X2, it can be written as:
- ⟨(X1, X2), {(3, 1), (3, 2), (2, 1)}⟩ or ⟨(X1, X2), X1 > X2⟩.

## Task to be Completed
1. Implement a Constraint Satisfaction Problem (CSP) in Python for the following problem:
   - Find all (x, y) pairs where x ∈ {1, 2, 3} and 0 <= y < 10, and x + y >= 5.
   - Solve the 4-Queen problem and Sudoku.
2. For the 4-Queen problem and Sudoku:
   - Identify the variables in the above problem.
   - Identify the set of constraint variables.
   - Identify the domain for each variable.

## Output
Here are two screenshots showcasing the output obtained from running the program:

- One screenshot with the constraint py file.

![With Constraint Screenshot](https://user-images.githubusercontent.com/57552973/209365275-848115ff-d33b-4516-98cb-6528f521cf79.png)

- Another screenshot without the constraint py file.

![Without Constraint Screenshot](https://user-images.githubusercontent.com/57552973/209365318-22501a53-ebab-4e04-b176-848413694c69.png)


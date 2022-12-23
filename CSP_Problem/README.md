A.1
Aim: 
a. Implement a Constraint Satisfaction Problem (CSP) in Python for the following problem
Find all (x,y) where x ∈ {1,2,3} and 0 <= y < 10, and x + y >= 5
b. For 4-Queen problem and Sudoku -
i. Identify the variables in the above problem
ii. Identify set of constraint variables
iii. Identify domain each variable

A.2
Prerequisite: Basic understanding of constraint satisfaction problem

A.3
Learning Outcome:
After completing this experiment, you will be able to-
1. Formulate a CSP
2. Implement a small problem with constraints in Python

A.4
Theory:
A.4.1 Constraint Satisfaction Problem (CSP)
 CSP can be defined by set of three components- X,D,C
 X is set of variables {𝑋1
, 𝑋2 … . 𝑋𝑛
}
 D is a set of domains {𝐷1
, 𝐷2
, … 𝐷𝑛
} for each variable
 C is a set of constraints that specify allowable combination of values



A.4.2 Example-
 If 𝑋1 𝑎𝑛𝑑 𝑋2 have the same domain {1,2,3} then the constraint saying that 
𝑋1 > 𝑋2 can be written as
◼ ⟨(𝑋1, 𝑋2), {(3,1), (3,2), (2,1)}⟩ or ⟨(𝑋1, 𝑋2), 𝑋1 > 𝑋2⟩


A.5 Task to be completed: 
a. Implement a Constraint Satisfaction Problem (CSP) in Python for the following problem
b. For 4-Queen problem and Sudoku -
i. Identify the variables in the above problem
ii. Identify set of constraint variables
iii. Identify domain each variable















Output for with constraint py file:


![image](https://user-images.githubusercontent.com/57552973/209365275-848115ff-d33b-4516-98cb-6528f521cf79.png)




Output for without constraint py file:



![image](https://user-images.githubusercontent.com/57552973/209365318-22501a53-ebab-4e04-b176-848413694c69.png)

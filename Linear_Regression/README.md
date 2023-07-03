# Simple Linear Regression

This README file provides instructions and information for implementing simple linear regression. The experiment involves using Python programming and various libraries.

## Table of Contents
1. [Aim](#aim)
2. [Prerequisite](#prerequisite)
3. [Outcome](#outcome)
4. [Theory](#theory)
5. [Task 1: Implementing Simple Linear Regression using NumPy](#task-1)
6. [Task 2: Implementing Simple Linear Regression using Sklearn](#task-2)
7. [Task 3: Implementing Simple Linear Regression with Dataset](#task-3)

<a name="aim"></a>
## Aim
The aim of this project is to implement simple linear regression.

<a name="prerequisite"></a>
## Prerequisite
In order to complete this experiment, you should have prior knowledge of Python programming, Pandas library, Numpy library, Matplotlib, and Seaborn library.

<a name="outcome"></a>
## Outcome
After successfully completing this experiment, you will be able to:
1. Implement simple linear regression using NumPy arrays.
2. Implement and verify the results using the Sklearn package.

<a name="theory"></a>
## Theory
### Linear Regression
Linear regression is a mathematical approach used to find the relationship between two or more variables. It is commonly used in machine learning to predict the behavior of a target variable based on the value of one or more predictor variables.

In simple linear regression, there is a single input variable (x) and the goal is to find a linear relationship between the input variable and the target variable (y). The relationship is represented by the equation: y = b0 + b1*x, where b0 is the intercept or bias coefficient, and b1 is the slope coefficient.

Tasks are provided to demonstrate the implementation of simple linear regression using NumPy arrays and the Sklearn package.

<a name="task-1"></a>
## Task 1: Implementing Simple Linear Regression using NumPy
Perform the following tasks to implement simple linear regression using NumPy arrays:

1. Define two NumPy arrays: x = [5, 15, 25, 35, 45, 55] and y = [11, 16, 18, 30, 22, 38].
2. Plot a scatter plot of x and y.
3. Compute the values of the coefficients of linear regression, b0 and b1.
4. Determine the value of r2.
5. Determine the predicted value of y for x = 20.
6. Plot the regression line on the scatter plot.

<a name="task-2"></a>
## Task 2: Implementing Simple Linear Regression using Sklearn
Perform the following tasks to implement simple linear regression using the Sklearn package:

1. Import LinearRegression from Sklearn.
2. Reshape x to make it a two-dimensional array.
3. Create a model for linear regression.
4. Train the model using the `fit()` function.
5. Determine the value of r2. Compare the value with the one obtained in Task 1.
6. Determine the value of the intercept (b0) and slope (b1). Compare the values as obtained from Task 1.

<a name="task-3"></a>
## Task 3: Implementing Simple Linear Regression with Dataset
Perform the following tasks to implement simple linear regression with a dataset:

1. Import `sat_cgpa.csv` into your notebook.
2. Explore the dataset using the `head()` and `describe()` functions.
3. Repeat steps 2 to 6 from Task 2 using the dataset.
4. Import `statsmodels.api`.
5. Plot a scatter plot of SAT vs GPA.
6. Convert SAT into a two-dimensional array.
7. Use the `OLS` function from `statsmodels` to fit the training data to the model.
8. Print the summary of the OLS regression model.
9. Interpret the results of the OLS regression model.

Please follow the instructions above to implement simple linear regression using NumPy and Sklearn, and analyze the results using the provided dataset.
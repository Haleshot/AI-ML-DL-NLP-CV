# Multiple Linear Regression

This README file provides instructions and information for implementing multiple linear regression. The experiment requires knowledge of multiple linear regression concepts and aims to develop skills in implementing and interpreting the results of different models.

## Table of Contents
1. [Aim](#aim)
2. [Prerequisite](#prerequisite)
3. [Outcome](#outcome)
4. [Theory](#theory)
5. [Task 1: Relationships between the different features](#task-1)
6. [Task 2: Fitting different simple linear regression models](#task-2)
7. [Task 3: Multiple regression model](#task-3)
8. [Task 4: Multiple regression model on 50 startups dataset](#task-4)

<a name="aim"></a>
## Aim
The aim of this project is to implement multiple linear regression.

<a name="prerequisite"></a>
## Prerequisite
To successfully complete this experiment, you should have a good understanding of multiple linear regression concepts.

<a name="outcome"></a>
## Outcome
After successfully completing this experiment, you will be able to:
1. Implement multiple linear regression using the `sklearn` package and `statsmodels`.
2. Interpret the results obtained from different models and choose the best model for a given dataset.

<a name="theory"></a>
## Theory
### Linear Regression
Multiple regression is an extension of simple linear regression. In multiple linear regression, a linear regression model contains more than one predictor variable. The model varies linearly with the change in the parameters β0, β1, β2, and so on. The intercept of the plane is represented by the parameter β0, while parameters β1, β2, etc. are referred to as partial regression coefficients.

The steps for multiple linear regression are as follows:
1. Identify the independent and dependent variables.
2. Check the relationships between the independent variables and the dependent variable using scatter plots and correlations.
3. Check the relationships between the independent variables using scatter plots and correlations.
4. Conduct simple linear regression for each independent variable-dependent variable pair.
5. Use the non-redundant independent variables in the analysis to find the best fitting model.
6. Use the best fitting model to make predictions about the dependent variable.

Tasks are provided to help you understand and implement multiple linear regression.

<a name="task-1"></a>
## Task 1: Relationships between the different features
Perform the following tasks to understand the relationships between the different features:

1. Import the relevant libraries.
2. Load the `MLR_data.csv` dataset into your notebook.
3. Perform exploratory data analysis (EDA) on the dataset using the `head()`, `shape`, and `describe()` functions.
4. Identify the independent variables (IV) and dependent variable (DV) and plot scatter plots of IV vs. DV. Write your inferences for each plot.
5. Plot scatter plots for IV vs. IV. Write your inferences for each plot.

<a name="task-2"></a>
## Task 2: Fitting different simple linear regression models
Perform the following tasks to fit different simple linear regression models for each IV/DV pair:

1. Import `LinearRegression` from `sklearn`.
2. Create a model for linear regression.
3. Conduct simple linear regression for each IV/DV pair:
   - Interest rate vs. stock index price
   - Unemployment vs. stock index price
4. Determine and tabulate the values of R2, slope, and intercept for each model.
5. Determine the predicted value of stock index price for an interest rate of 2.75.
6. Determine the predicted value of stock index price for an unemployment rate of 6.
7

. Compare both models based on R2 and the mean square error between predicted and actual stock index price.

<a name="task-3"></a>
## Task 3: Multiple regression model
Perform the following tasks to create a multiple regression model:

1. Use both interest rate and unemployment rate as independent variables and create a multiple regression model.
2. Determine the value of R2, slope, and intercept for the model.
3. Determine the predicted value of stock index price for:
   - Interest rate = 2.75 and unemployment rate = 5.3
   - Interest rate = 2 and unemployment rate = 6
4. Compare the model with the models from Task 2.
5. Identify and state the best model for the dataset.

<a name="task-4"></a>
## Task 4: Multiple regression model on 50 startups dataset
Perform the following tasks to create a multiple regression model on the 50 startups dataset:

1. Load the 50 startups dataset.
2. Follow the steps mentioned in the theory for multiple linear regression to determine the best fitting model for this dataset.

> [!NOTE]
> Make sure to follow the instructions provided for each task and analyze the results accordingly to gain a better understanding of multiple linear regression.

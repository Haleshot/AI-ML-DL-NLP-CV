# Data Exploration using Pandas Library

This README file provides instructions and information for understanding and implementing data exploration techniques using the Pandas library. The following tasks will be performed on a car dataset:

## Table of Contents
1. [Aim](#aim)
2. [Prerequisite](#prerequisite)
3. [Outcome](#outcome)
4. [Theory](#theory)
5. [Task 1: Exploratory Data Analysis on Car Dataset](#task-1)
6. [Task 2: One Hot and Label Encoding on "adults" Dataset](#task-2)

<a name="aim"></a>
## Aim
The aim of this project is to understand and implement data exploration techniques using the Pandas library.

<a name="prerequisite"></a>
## Prerequisite
In order to complete this experiment, you should have prior knowledge of Python programming and the Pandas library.

<a name="outcome"></a>
## Outcome
After successfully completing this experiment, you will be able to:
- Read different types of data files (csv, excel, text file, etc.).
- Obtain metadata of a given dataset.
- Understand finding null values and replacing them.
- Understand and implement class label encoding.
- Understand and implement one hot encoding.

<a name="theory"></a>
## Theory
### Exploratory Data Analysis (EDA)
Exploratory Data Analysis (EDA) is an open-ended process where we calculate statistics and make figures to find trends, anomalies, patterns, or relationships within the data. The goal of EDA is to learn what our data can tell us. It generally starts out with a high-level overview, then narrows in to specific areas as we find intriguing areas of the data. The findings may be interesting in their own right, or they can be used to inform our modeling choices, such as by helping us decide which features to use.

### Pandas Library
Pandas is a powerful Python library for data manipulation and analysis. It provides a DataFrame, which is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. The DataFrame accepts many different kinds of input, including dictionaries, lists, arrays, and other DataFrames.

### Encoding
#### One Hot Encoding
One-hot encoding converts categorical data into numeric data by splitting the column into multiple columns. Each unique value in the column becomes a new column, and the values are replaced by 1s and 0s, depending on which column has what value.

#### Label Encoding
Label encoding is a simple approach that involves converting each value in a column into a number. Each unique value is assigned a unique integer label.

<a name="task-1"></a>
## Task 1: Exploratory Data Analysis on Car Dataset
Perform the following exploratory data analysis tasks on the car dataset:

1. Read the Toyota.csv file into a DataFrame.
2. Explore the size, shape, and data types of each column in the dataset.
3. List down the columns of the dataset.
4. Find out the 'Fuel Type' for the 4th row.
5. Find out the value for the second column for the 4th row.
6. Select all rows for the column "Fuel Type".
7. Select all rows for the columns "KM", "HP", and "Automatic".
8. Display the first five rows for columns 2 to 4 (excluding row 5 and column 4).
9. Display the info of the dataset and state your observations.
10. Identify unique values for the columns "KM", "HP", and "Doors".
11. Create a new data frame, replacing "???" with NaN.
12. Replace the categorical values in the "Doors" column with their corresponding numeric values.
13. Convert the data types of columns "Doors", "MetColor", and "Automatic" to int and object.
14. Identify the total number of null values in each column of the dataset.
15. Drop rows with null values.
16. Identify the total number of cars that run on "Petrol", "Diesel", or "CNG".
17. Identify the mean of "KM" for the cars that run on "Diesel".

<a name="task-2"></a>
## Task 2: One Hot and Label Encoding on "adults" Dataset
Perform one hot encoding and label encoding on the relationship column of the "adults" dataset.

---
Please follow the instructions above to perform the data exploration tasks using Pandas library.

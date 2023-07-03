# K-Nearest Neighbor (KNN) Algorithm for Classification

This README file provides instructions and information for implementing the KNN algorithm for classification. The experiment requires prior knowledge of Python programming and the following libraries: Pandas, NumPy, Matplotlib, and Seaborn.

## Table of Contents
1. [Aim](#aim)
2. [Prerequisite](#prerequisite)
3. [Outcome](#outcome)
4. [Theory](#theory)
5. [Task 1: Implementing KNN Algorithm](#task-1)
6. [Task 2: Operations on Social_Network_Ads.csv Dataset](#task-2)
7. [Task 3: Implementing KNN Algorithm on Sklearn Dataset](#task-3)

<a name="aim"></a>
## Aim
The aim of this project is to implement the KNN algorithm for classification.

<a name="prerequisite"></a>
## Prerequisite
To successfully complete this experiment, you should have knowledge of Python programming and the following libraries: Pandas, NumPy, Matplotlib, and Seaborn.

<a name="outcome"></a>
## Outcome
After successfully completing this experiment, you will be able to:
1. Implement the KNN technique for classification.

<a name="theory"></a>
## Theory
### K-Nearest Neighbor (KNN)
KNN is one of the simplest machine learning algorithms based on the supervised learning technique. It assumes similarity between new data and available data and assigns the new case to the category that is most similar to the available categories. KNN can be used to classify new data into suitable categories.

The steps involved in KNN are as follows:
1. Step 1: Select the number K of neighbors.
2. Step 2: Calculate the Euclidean distance of K number of neighbors.
3. Step 3: Take the K nearest neighbors based on the calculated Euclidean distance.
4. Step 4: Count the number of data points in each category among these K neighbors.
5. Step 5: Assign the new data points to the category for which the number of neighbors is maximum.
6. Step 6: Model is ready!

To determine a good value of K:
- It is generally determined experimentally.
- Initialize K with 1 and use the test set for classifier validation (accuracy).
- Increment the value of K and repeat the procedure.
- Choose the value of K that shows the minimum error.

Feature transformation is an important aspect of KNN. It involves normalizing or standardizing the data to fall within a smaller or common range. This helps prevent attributes with initially large ranges from outweighing attributes with initially smaller ranges.

Tasks are provided to help you understand and implement the KNN algorithm.

<a name="task-1"></a>
## Task 1: Implementing KNN Algorithm
Perform the following tasks to implement the KNN algorithm:

For the test data (1,1), determine the class using:
- 3-KNN
- 5-KNN
- 7-KNN

Use the provided dataset as the training dataset. Write your own user-defined function to implement KNN.

<a name="task-2"></a>
## Task 2: Operations on Social_Network_Ads.csv Dataset
Perform the following tasks on the given `Social_Network_Ads.csv` dataset:

1. Upload the dataset and store it in a Pandas DataFrame.
2. Explore the dataset using the `head()`, `describe()`, and `size` commands.
3. Identify the input features and output feature.
4. Identify the total number of classes in the output feature.
5. Remove columns that are not useful for classification.
6. Convert categorical columns into numeric columns.
7. Apply scalar transformation.

<a name="task-3"></a>
## Task 3: Implementing KNN Algorithm on Sklearn Dataset
Perform the following tasks to implement the KNN algorithm on the given dataset from the Sklearn library with K=5:

1. Split the dataset into train and test sets.
2. Fit the KNN model on the train dataset.
3. Identify the class for the test dataset.
4. Print the confusion matrix.
5. Print the accuracy score.
6. Write your inference based on the results.

Follow the instructions provided for each task and analyze the results to gain a better understanding of the KNN algorithm.
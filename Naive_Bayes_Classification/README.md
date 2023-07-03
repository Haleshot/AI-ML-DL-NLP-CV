# Naïve Bayes Algorithm for Classification

This README file provides instructions and information for implementing the Naïve Bayes algorithm for classification. The experiment requires prior knowledge of Python programming and the following libraries: Pandas, NumPy, Matplotlib, and Seaborn.

## Table of Contents
1. [Aim](#aim)
2. [Prerequisite](#prerequisite)
3. [Outcome](#outcome)
4. [Theory](#theory)
5. [Tasks](#tasks)

<a name="aim"></a>
## Aim
The aim of this project is to implement the Naïve Bayes algorithm for classification.

<a name="prerequisite"></a>
## Prerequisite
To successfully complete this experiment, you should have knowledge of Python programming and the following libraries: Pandas, NumPy, Matplotlib, and Seaborn.

<a name="outcome"></a>
## Outcome
After successfully completing this experiment, you will be able to:
1. Implement the Naïve Bayes technique for classification.
2. Compare the results of Naïve Bayes and KNN algorithms.
3. Understand and infer the results of different classification metrics.

<a name="theory"></a>
## Theory
### Naïve Bayes Classifier
The Naïve Bayes algorithm is a supervised learning algorithm based on Bayes' theorem. It is used for solving classification problems and is particularly effective for text classification with high-dimensional training datasets. The Naïve Bayes Classifier is a simple yet effective classification algorithm that can build fast machine learning models for quick predictions. It is a probabilistic classifier that predicts based on the probability of an object. Examples of Naïve Bayes applications include spam filtration, sentiment analysis, and article classification.

### Bayes' Theorem
Bayes' theorem, also known as Bayes' Rule or Bayes' law, is used to determine the probability of a hypothesis given prior knowledge. It relies on conditional probability. The formula for Bayes' theorem is as follows:

```
P(A|B) = (P(B|A) * P(A)) / P(B)
```

Where:
- P(A|B) is the posterior probability: the probability of hypothesis A given the observed event B.
- P(B|A) is the likelihood probability: the probability of the evidence given that the probability of a hypothesis A is true.
- P(A) is the prior probability: the probability of the hypothesis before observing the evidence.
- P(B) is the marginal probability: the probability of the evidence.

### Working of Naïve Bayes Classifier
The working of the Naïve Bayes Classifier involves the following steps:
1. Convert the given dataset into frequency tables.
2. Generate a likelihood table by finding the probabilities of given features.
3. Use Bayes' theorem to calculate the posterior probability.

<a name="tasks"></a>
## Tasks
Perform the following tasks to implement the Naïve Bayes algorithm and compare it with KNN:

Task 1: Implementing Naïve Bayes Algorithm on Car Dataset
- Apply the Naïve Bayes algorithm to the given car dataset.
- Show all the steps of the training phase.
- Identify the class for the test data point (color = Yellow, Type = Sports, Origin = Domestic).
- Solve the answer on paper and upload the image.

Task 2: Operations on Adult.csv Dataset
- Upload the dataset into a dataframe.
- Check the shape of the dataset.
- Find out all the categorical columns from the dataset.
- Check if null values exist in all the categorical columns.
- Identify the problems with the "workclass," "Occupation," and "native_country" columns and rectify them.
- Explore numeric columns and check for any null values.
- Create a feature vector with x = all the columns except income and y = income.
- Implement feature engineering for the train-test split dataset:
  - Check the data types of columns of the input features of the training dataset.
  - Identify categorical columns that have null values and fill them with the most probable value in the dataset.
  - Repeat the above step for the input features of the test dataset.
  - Apply one-hot encoding on all the categorical columns.
  - Apply feature scaling using a robust scaler.

Task 3: Implement KNN Algorithm on Sklearn Dataset with k=5.

Task 4: Implement Naïve Bayes Algorithm on the given dataset.

Task 5: Compare the confusion matrix for both classifiers.

Task 6: Compare the accuracy score of both classifiers.

Task 7: Draw the ROC curve to compare both models.

Follow the instructions provided for each task and analyze the results to gain a better understanding of the Naïve Bayes algorithm and its comparison with KNN.
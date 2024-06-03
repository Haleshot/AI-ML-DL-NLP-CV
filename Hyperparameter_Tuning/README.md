# Deep Learning: Hyperparameter Tuning

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Steps](#steps)
  - [Step 1: Import the IMDB data from Keras](#step-1-import-the-imdb-data-from-keras)
  - [Step 2: Pre-processing and prepare the data](#step-2-pre-processing-and-prepare-the-data)
    - [Step 2a: Encoding the integer sequences into a binary matrix](#step-2a-encoding-the-integer-sequences-into-a-binary-matrix)
    - [Step 2b: Split it into train and test](#step-2b-split-it-into-train-and-test)
    - [Step 2c: Set aside validation data from the training set](#step-2c-set-aside-validation-data-from-the-training-set)
  - [Step 3: Building the sequential neural network model](#step-3-building-the-sequential-neural-network-model)
    - [Step 3a: You may choose the layers](#step-3a-you-may-choose-the-layers)
    - [Step 3b: Use appropriate activation and loss functions](#step-3b-use-appropriate-activation-and-loss-functions)
  - [Step 4: Compile and fit the model to the training dataset](#step-4-compile-and-fit-the-model-to-the-training-dataset)
  - [Step 5: Plot training and validation loss](#step-5-plot-training-and-validation-loss)
  - [Step 6: Use regularizers to improve the performance](#step-6-use-regularizers-to-improve-the-performance)
  - [Step 7: Record the best performance](#step-7-record-the-best-performance)

## Aim
To perform hyperparameter tuning on a neural network model using the IMDB dataset.

## Prerequisite
- Python Programming
- Numpy
- Pandas
- TensorFlow/Keras

## Steps

### Step 1: Import the IMDB data from Keras
Import the IMDB dataset using Keras.

### Step 2: Pre-processing and prepare the data

#### Step 2a: Encoding the integer sequences into a binary matrix
Encode the integer sequences into a binary matrix for neural network input.

#### Step 2b: Split it into train and test
Split the dataset into training and testing sets.

#### Step 2c: Set aside validation data from the training set
Set aside a portion of the training data to be used as validation data.

### Step 3: Building the sequential neural network model

#### Step 3a: You may choose the layers
Choose the layers for the sequential neural network model.

#### Step 3b: Use appropriate activation and loss functions
Select appropriate activation and loss functions for the neural network.

### Step 4: Compile and fit the model to the training dataset
Compile and fit the model to the training dataset, incorporating validation data as well.

### Step 5: Plot training and validation loss
Plot the training and validation loss to monitor the model's performance over epochs.

### Step 6: Use regularizers to improve the performance
Apply regularizers to the model to enhance performance and prevent overfitting.

### Step 7: Record the best performance
Document the best performance achieved during the tuning process.

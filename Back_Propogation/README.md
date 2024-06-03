# Deep Learning: Implementation of Back Propagation

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Steps](#steps)
  - [Step 1: Load the IRIS dataset](#step-1-load-the-iris-dataset)
  - [Step 2: Pre-processing of the dataset](#step-2-pre-processing-of-the-dataset)
    - [Step 2a: Convert categorical values to numeric values](#step-2a-convert-categorical-values-to-numeric-values)
    - [Step 2b: Remove the species column and append the one hot encoded columns](#step-2b-remove-the-species-column-and-append-the-one-hot-encoded-columns)
    - [Step 2c: Scale the four feature columns](#step-2c-scale-the-four-feature-columns)
  - [Step 3: Building the three-layer feedforward neural network](#step-3-building-the-three-layer-feedforward-neural-network)
    - [Step 3a: Build the three-layer feedforward neural network](#step-3a-build-the-three-layer-feedforward-neural-network)
    - [Step 3b: No. of neurons in hidden layer](#step-3b-no-of-neurons-in-hidden-layer)
    - [Step 3c: Initialize the network with random weights and biases](#step-3c-initialize-the-network-with-random-weights-and-biases)
    - [Step 3d: Use sigmoid as the activation function](#step-3d-use-sigmoid-as-the-activation-function)
    - [Step 3e: Use loss function as MSE](#step-3e-use-loss-function-as-mse)
    - [Step 3f: Compute the MSE and accuracy](#step-3f-compute-the-mse-and-accuracy)
  - [Step 4: Implement backpropagation for this network](#step-4-implement-backpropagation-for-this-network)
    - [Step 4a: Use learning rate as 0.01](#step-4a-use-learning-rate-as-001)
    - [Step 4b: No. of iterations as 5000](#step-4b-no-of-iterations-as-5000)
    - [Step 4c: Plot the MSE and accuracy](#step-4c-plot-the-mse-and-accuracy)
  - [Step 5: Change the learning rate and no. of iterations and note the performance](#step-5-change-the-learning-rate-and-no-of-iterations-and-note-the-performance)
    - [Performance Table](#performance-table)

## Aim
To implement back propagation in a three-layer feedforward neural network using the IRIS dataset.

## Prerequisite
- Python Programming
- Numpy
- Pandas
- Scikit-learn
- TensorFlow/Keras

## Steps

### Step 1: Load the IRIS dataset
Load the IRIS dataset available on Kaggle into your notebooks.

### Step 2: Pre-processing of the dataset

#### Step 2a: Convert categorical values to numeric values
Convert the categorical values to numeric values using one hot encoder.

#### Step 2b: Remove the species column and append the one hot encoded columns
Remove the species column from the original dataset and append the one hot encoded columns to the data frame.

#### Step 2c: Scale the four feature columns
Scale the four feature columns of the data frame using standard scaler.

### Step 3: Building the three-layer feedforward neural network

#### Step 3a: Build the three-layer feedforward neural network
Build the three-layer feedforward neural network, using sigmoid as the activation function.

#### Step 3b: No. of neurons in hidden layer
No. of neurons in the hidden layer are 2.

#### Step 3c: Initialize the network with random weights and biases
Initialize the network with random weights and biases.

#### Step 3d: Use sigmoid as the activation function
Use sigmoid as the activation function.

#### Step 3e: Use loss function as MSE
Use loss function as Mean Squared Error (MSE).

#### Step 3f: Compute the MSE and accuracy
Compute the Mean Squared Error (MSE) and accuracy of the network.

### Step 4: Implement backpropagation for this network

#### Step 4a: Use learning rate as 0.01
Set the learning rate to 0.01.

#### Step 4b: No. of iterations as 5000
Set the number of iterations to 5000.

#### Step 4c: Plot the MSE and accuracy
Plot the MSE and accuracy over the iterations.

### Step 5: Change the learning rate and no. of iterations and note the performance
Change the learning rate and the number of iterations and note the performance. Highlight the optimum performance.

#### Performance Table
![Performance Table](image.png)

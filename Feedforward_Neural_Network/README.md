# Deep Learning

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
    - [Step 3a: Build the neural network and use sigmoid as the activation](#step-3a-build-the-neural-network-and-use-sigmoid-as-the-activation)
    - [Step 3b: Initialize the weights and biases](#step-3b-initialize-the-weights-and-biases)
    - [Step 3c: Compute the output of the hidden layer](#step-3c-compute-the-output-of-the-hidden-layer)
    - [Step 3d: Compute the output of the final layer](#step-3d-compute-the-output-of-the-final-layer)
  - [Step 4: Error calculation](#step-4-error-calculation)
    - [Step 4a: Compute the total squared error](#step-4a-compute-the-total-squared-error)
  - [Step 5: Change the initial weights and biases and compute the error again](#step-5-change-the-initial-weights-and-biases-and-compute-the-error-again)
  - [Step 6: Add one more hidden neuron in the middle layer and compare the error](#step-6-add-one-more-hidden-neuron-in-the-middle-layer-and-compare-the-error)

## Aim
To implement a feedforward neural network and understand its workings through a series of steps.

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

#### Step 3a: Build the neural network and use sigmoid as the activation
Build the three-layer feedforward neural network, using sigmoid as the activation function.

#### Step 3b: Initialize the weights and biases
Initialize the weights and biases for the network.

#### Step 3c: Compute the output of the hidden layer
Compute the output of the hidden layer in the network.

#### Step 3d: Compute the output of the final layer
Compute the output of the final layer in the network.

### Step 4: Error calculation

#### Step 4a: Compute the total squared error
Compute the total squared error for the network.

### Step 5: Change the initial weights and biases and compute the error again
Change the initial weights and biases and compute the error again to observe the differences.

### Step 6: Add one more hidden neuron in the middle layer and compare the error
Add one more hidden neuron in the middle layer of the network and compare the error to previous configurations.

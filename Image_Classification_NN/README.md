# Image Classification using Fashion MNIST Dataset

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Steps](#steps)
  - [Step 1: Load the Fashion MNIST dataset into your notebook](#step-1-load-the-fashion-mnist-dataset-into-your-notebook)
  - [Step 2: Pre-processing and prepare the data for giving to the neural network](#step-2-pre-processing-and-prepare-the-data-for-giving-to-the-neural-network)
    - [Step 2a: Explore the dataset](#step-2a-explore-the-dataset)
    - [Step 2b: Determine the number of classes](#step-2b-determine-the-number-of-classes)
    - [Step 2c: Normalize the dataset and flatten it to be suitable for applying to an ANN](#step-2c-normalize-the-dataset-and-flatten-it-to-be-suitable-for-applying-to-an-ann)
    - [Step 2d: Split the dataset into train and test](#step-2d-split-the-dataset-into-train-and-test)
  - [Step 3: Building the sequential neural network model](#step-3-building-the-sequential-neural-network-model)
    - [Step 3a: You may choose the layers](#step-3a-you-may-choose-the-layers)
    - [Step 3b: Use appropriate activation and loss functions](#step-3b-use-appropriate-activation-and-loss-functions)
  - [Step 4: Compile and fit the model to the training dataset](#step-4-compile-and-fit-the-model-to-the-training-dataset)
  - [Step 5: Apply regularization and see the effect on the performance](#step-5-apply-regularization-and-see-the-effect-on-the-performance)
  - [Step 6: Use different optimizers and record the best performance](#step-6-use-different-optimizers-and-record-the-best-performance)

## Aim
To perform image classification on the Fashion MNIST dataset using a neural network.

## Prerequisite
- Python Programming
- Keras
- TensorFlow
- Numpy

## Steps

### Step 1: Load the Fashion MNIST dataset into your notebook
Load the Fashion MNIST dataset to begin the data processing and modeling steps.
- Load it using `from keras.datasets import fashion_mnist`

### Step 2: Pre-processing and prepare the data for giving to the neural network

#### Step 2a: Explore the dataset
Explore the dataset to understand its structure and the type of data it contains.

#### Step 2b: Determine the number of classes
Identify the number of unique classes in the dataset to guide the model architecture.

#### Step 2c: Normalize the dataset and flatten it to be suitable for applying to an ANN
Normalize the feature values to ensure they fall within a specific range and flatten the images to be compatible with an Artificial Neural Network (ANN).

#### Step 2d: Split the dataset into train and test
Split the dataset into training and testing sets to evaluate the model's performance.

### Step 3: Building the sequential neural network model

#### Step 3a: You may choose the layers
Select and add layers to the sequential neural network model as per requirement.

#### Step 3b: Use appropriate activation and loss functions
Choose suitable activation and loss functions for the neural network.

### Step 4: Compile and fit the model to the training dataset
Compile and fit the model to the training dataset, and include validation data in the process.

### Step 5: Apply regularization and see the effect on the performance
Apply regularization techniques such as L2 regularization or dropout to the model and observe their effects on performance.

### Step 6: Use different optimizers and record the best performance
Experiment with different optimizers like SGD, Momentum-based optimizer, Adagrad, Adam, and RMSprop. Record and compare their performances to determine the best optimizer for your model.

# Deep Learning

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Steps](#steps)
  - [Step 1: Load the IRIS dataset into your notebook](#step-1-load-the-iris-dataset-into-your-notebook)
  - [Step 2: Pre-processing and prepare the data for giving to the neural network](#step-2-pre-processing-and-prepare-the-data-for-giving-to-the-neural-network)
    - [Step 2a: Encoding the species names using label encoder](#step-2a-encoding-the-species-names-using-label-encoder)
    - [Step 2b: Normalize the features](#step-2b-normalize-the-features)
    - [Step 2c: Split it into train and validate](#step-2c-split-it-into-train-and-validate)
  - [Step 3: Building the sequential neural network model](#step-3-building-the-sequential-neural-network-model)
    - [Step 3a: You may choose the layers](#step-3a-you-may-choose-the-layers)
    - [Step 3b: Use appropriate activation and loss functions](#step-3b-use-appropriate-activation-and-loss-functions)
  - [Step 4: Compile and fit the model to the training dataset](#step-4-compile-and-fit-the-model-to-the-training-dataset)
  - [Step 5: Use learning rates as (0.1, 0.01, 0.001, 0.0001)](#step-5-use-learning-rates-as-01-001-0001-00001)
  - [Step 6: Use the best learning rate and add momentum to it](#step-6-use-the-best-learning-rate-and-add-momentum-to-it)
  - [Step 7: Add a decay parameter to the optimizer](#step-7-add-a-decay-parameter-to-the-optimizer)
  - [Step 8: Train the model using Adagrad, Adam, and RMSprop](#step-8-train-the-model-using-adagrad-adam-and-rmsprop)
  - [Step 9: Infer the best optimizer and learning rate for your model](#step-9-infer-the-best-optimizer-and-learning-rate-for-your-model)
  - [Step 10: Repeat the above steps on seeds dataset](#step-10-repeat-the-above-steps-on-seeds-dataset)

## Aim
To perform various optimization techniques on a neural network using the IRIS dataset and evaluate their performances.

## Prerequisite
- Python Programming
- Numpy
- Pandas
- TensorFlow/Keras

## Steps

### Step 1: Load the IRIS dataset into your notebook
Load the IRIS dataset to begin the data processing and modeling steps.

### Step 2: Pre-processing and prepare the data for giving to the neural network

#### Step 2a: Encoding the species names using label encoder
Encode the species names using a label encoder to convert categorical values into numerical values.

#### Step 2b: Normalize the features
Normalize the feature values to ensure that they have a mean of 0 and a standard deviation of 1.

#### Step 2c: Split it into train and validate
Split the dataset into training and validation sets to evaluate the model's performance.

### Step 3: Building the sequential neural network model

#### Step 3a: You may choose the layers
Select and add layers to the sequential neural network model as per requirement.

#### Step 3b: Use appropriate activation and loss functions
Choose suitable activation and loss functions for the neural network.

### Step 4: Compile and fit the model to the training dataset
Compile and fit the model to the training dataset using Stochastic Gradient Descent (SGD) as the optimizer, and include validation data in the process.

### Step 5: Use learning rates as (0.1, 0.01, 0.001, 0.0001)
Train the model using different learning rates (0.1, 0.01, 0.001, 0.0001). Plot the training and validation accuracy curves and determine the best learning rate.

### Step 6: Use the best learning rate and add momentum to it
Using the best learning rate identified, add momentum values (0, 0.5, 0.9, 0.99) to the optimizer. Train the model and identify the best momentum value.

### Step 7: Add a decay parameter to the optimizer
Introduce a decay parameter to the optimizer with values (1E-1, 1E-2, 1E-3, 1E-4) and note the performance improvements.

### Step 8: Train the model using Adagrad, Adam, and RMSprop
Train the model using different optimizers such as Adagrad, Adam, and RMSprop to determine which one works best.

### Step 9: Infer the best optimizer and learning rate for your model
Evaluate and infer the best optimizer and learning rate combination that yields the highest performance for the neural network model.

### Step 10: Repeat the above steps on seeds dataset
Repeat all the above steps using the seeds dataset to compare the performance and effectiveness of the different optimizers and learning rates on a different dataset.

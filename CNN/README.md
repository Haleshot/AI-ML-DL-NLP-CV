# Build and Train a Convolutional Neural Network (CNN) and Explore Different Layers

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Steps](#steps)
  - [Step 1: Load the MNIST dataset into your notebook](#step-1-load-the-mnist-dataset-into-your-notebook)
  - [Step 2: Pre-processing and prepare the data for giving to the CNN](#step-2-pre-processing-and-prepare-the-data-for-giving-to-the-cnn)
    - [Step 2a: Encoding the classes using one hot encoder](#step-2a-encoding-the-classes-using-one-hot-encoder)
    - [Step 2b: Normalize the features](#step-2b-normalize-the-features)
  - [Step 3: Building the convolutional network model](#step-3-building-the-convolutional-network-model)
    - [Step 3a: You may choose the layers](#step-3a-you-may-choose-the-layers)
    - [Step 3b: Print the summary and note the number of neurons and parameters of the model](#step-3b-print-the-summary-and-note-the-number-of-neurons-and-parameters-of-the-model)
    - [Step 3c: Compile the model and train it using the training data](#step-3c-compile-the-model-and-train-it-using-the-training-data)
  - [Step 4: Vary the number of layers and repeat step 3](#step-4-vary-the-number-of-layers-and-repeat-step-3)
  - [Step 5: Implement the architecture of LeNet 5](#step-5-implement-the-architecture-of-lenet-5)
  - [Step 6: Finally note which network gives you the best performance](#step-6-finally-note-which-network-gives-you-the-best-performance)

## Aim
To build and train a Convolutional Neural Network (CNN) on the MNIST dataset and explore the application of different layers.

## Prerequisite
- Python Programming
- TensorFlow/Keras
- Convolutional Neural Networks (CNNs)
- MNIST dataset

## Steps

### Step 1: Load the MNIST dataset into your notebook
Load the MNIST dataset to begin the data processing and modeling steps.

### Step 2: Pre-processing and prepare the data for giving to the CNN

#### Step 2a: Encoding the classes using one hot encoder
Convert the class labels into a binary matrix representation using one hot encoding.

#### Step 2b: Normalize the features
Normalize the pixel values of the images to a range between 0 and 1.

### Step 3: Building the convolutional network model

#### Step 3a: You may choose the layers
Select and add layers to the CNN model as per requirement, including convolutional layers, pooling layers, and dense layers.

#### Step 3b: Print the summary and note the number of neurons and parameters of the model
Display the summary of the CNN model architecture and note the number of neurons and parameters for each layer.

#### Step 3c: Compile the model and train it using the training data
Compile the CNN model with appropriate loss function, optimizer, and metrics. Train the model using the training dataset, and include validation data for evaluation during training.

### Step 4: Vary the number of layers and repeat step 3
Experiment by adding or removing layers from the CNN model architecture and observe the impact on model performance.

### Step 5: Implement the architecture of LeNet 5
Implement the specific architecture of LeNet 5, a classic CNN architecture designed for handwritten digit recognition.

### Step 6: Finally note which network gives you the best performance
Compare the performance of different CNN architectures (varying layers and LeNet 5) based on metrics such as accuracy and loss to determine which network performs the best for the MNIST dataset.

# Support Vector Machines (SVM)

This README file provides information on Support Vector Machines (SVM) and its implementation. The SVM algorithm is used for classification and regression analysis. Below is a breakdown of the content covered in this README.

## Table of Contents
1. [Part A: Computing Support Vectors for a Dataset](#part-a)
2. [Part B: Creating an SVM Model with Linear Kernel](#part-b)
3. [Part C: Plotting SVC Decision Function](#part-c)
4. [Part D: Fetching LFW People Dataset](#part-d)
5. [Implementation of SVM with PCA](#implementation)
6. [Displaying Predicted Names and Labels](#displaying-names)
7. [Confusion Matrix and Heatmap](#confusion-matrix)

<a name="part-a"></a>
## Part A: Computing Support Vectors for a Dataset
In this section, we discuss the computation of support vectors for a given dataset. Support vectors are the data points that lie closest to the decision boundary of the SVM classifier.

<a name="part-b"></a>
## Part B: Creating an SVM Model with Linear Kernel
To create an SVM model with a linear kernel, the `SVC` class from the `sklearn.svm` module is used. The `kernel` parameter is set to 'linear', and the `C` parameter controls the regularization strength.

Example:
```python
from sklearn.svm import SVC

model = SVC(kernel='linear', C=1E10)
model.fit(X, y)
```

<a name="part-c"></a>
## Part C: Plotting SVC Decision Function
This section discusses the `plot_svc_decision_function` method, which allows visualizing the decision function of an SVM model.

<a name="part-d"></a>
## Part D: Fetching LFW People Dataset
The LFW People dataset is fetched using the `fetch_lfw_people` function from the `sklearn.datasets` module. This dataset contains face images of different individuals.

Example:
```python
from sklearn.datasets import fetch_lfw_people

faces = fetch_lfw_people(min_faces_per_person=60)
print(faces.target_names)
print(faces.images.shape)
```

<a name="implementation"></a>
## Implementation of SVM with PCA
In this section, an SVM model with a radial basis function (RBF) kernel is implemented using Principal Component Analysis (PCA) for dimensionality reduction. The `RandomizedPCA` class from `sklearn.decomposition` and the `make_pipeline` function from `sklearn.pipeline` are used.

Example:
```python
from sklearn.svm import SVC
from sklearn.decomposition import PCA as RandomizedPCA
from sklearn.pipeline import make_pipeline

pca = RandomizedPCA(n_components=150, whiten=True, random_state=42)
svc = SVC(kernel='rbf', class_weight='balanced')
model = make_pipeline(pca, svc)
```

<a name="displaying-names"></a>
## Displaying Predicted Names and Labels
This section demonstrates how to display predicted names and labels using a subplot layout. The face images are shown, and the predicted names are displayed with incorrect labels highlighted in red.

Example:
```python
fig, ax = plt.subplots(4, 6)
for i, axi in enumerate(ax.flat):
    axi.imshow(Xtest[i].reshape(62, 47), cmap='bone')
    axi.set(xticks=[], yticks=[])
    axi.set_ylabel(faces.target_names[yfit[i]].split()[-1], color='black' if yfit[i] == ytest[i] else 'red')
fig.suptitle('Predicted Names; Incorrect Labels in Red',

 size=14)
```

<a name="confusion-matrix"></a>
## Confusion Matrix and Heatmap
This section demonstrates how to create a confusion matrix using the `confusion_matrix` function from `sklearn.metrics`. The confusion matrix is visualized using a heatmap with labeled axes.

Example:
```python
import seaborn as sns
from sklearn.metrics import confusion_matrix

mat = confusion_matrix(ytest, yfit)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=faces.target_names, yticklabels=faces.target_names)
plt.xlabel('True Label')
plt.ylabel('Predicted Label')
```

Use the provided instructions and code examples to explore and understand the implementation of Support Vector Machines (SVM).
# Data Visualization Techniques

This README file provides instructions and information for understanding and implementing data visualization techniques. The following tasks will be performed using Python programming and various libraries:

## Table of Contents
1. [Aim](#aim)
2. [Prerequisite](#prerequisite)
3. [Outcome](#outcome)
4. [Theory](#theory)
5. [Task 1: Exploring Data Visualization](#task-1)
6. [Tasks 2-15: Various Plots and Analysis](#tasks-2-15)

<a name="aim"></a>
## Aim
The aim of this project is to understand and implement data visualization techniques.

<a name="prerequisite"></a>
## Prerequisite
In order to complete this experiment, you should have prior knowledge of Python programming, Pandas library, Numpy library, Matplotlib, and Seaborn library.

<a name="outcome"></a>
## Outcome
After successfully completing this experiment, you will be able to:
- Read different types of data files (csv, excel, text file, etc.).
- Understand the usage of different Python libraries for plotting data.
- Plot data using different types of plots.

<a name="theory"></a>
## Theory
Data visualization is a form of visual communication that involves creating and studying visual representations of data. It helps in understanding patterns, trends, and relationships within the data. In this project, we will be using Matplotlib and Seaborn libraries for data visualization.

### Matplotlib
Matplotlib is a widely used Python library for data visualization. It provides a comprehensive set of plotting tools and supports various types of plots such as scatter plots, bar charts, line plots, box plots, and more.

### Seaborn
Seaborn is a Python library based on Matplotlib that provides a high-level interface for creating attractive and informative statistical graphics. It simplifies the process of creating visually pleasing plots and supports advanced features like categorical plots, violin plots, joint plots, and more.

### Common Types of Plots
In this project, we will be using the following common types of plots for data visualization:

- Scatter Plot: A scatter plot visualizes the relationship between two continuous variables by displaying individual data points on a two-dimensional plane.
- Pair Plot: A pair plot creates a grid of scatter plots to visualize the relationships between multiple variables in a dataset.
- Box Plot: A box plot displays the distribution of quantitative data, showing the median, quartiles, and outliers.
- Violin Plot: A violin plot combines a box plot with a kernel density estimation to visualize the distribution of data.
- Distribution Plot: A distribution plot displays the distribution of a single variable using a histogram or a kernel density estimate.
- Joint Plot: A joint plot combines two distribution plots and a scatter plot to visualize the relationship between two variables.
- Bar Chart: A bar chart represents categorical data using rectangular bars with heights or lengths proportional to the values they represent.
- Line Plot: A line plot displays data points connected by straight lines, commonly used to show trends over time.

<a name="task-1"></a>
## Task 1: Exploring Data Visualization
Perform the following tasks to explore data visualization techniques:

1. Read the "seeds.csv" file into a DataFrame.
2. Explore the dataset using the head and describe functions.
3. Find the number of samples per type and plot a histogram for the count.

<a name="tasks-2-15"></a>
## Tasks 2-15: Various Plots and Analysis
Perform the following tasks to create different plots and analyze the dataset:

2. Plot a scatter plot for Kernel Width vs Length and write your inference.
3. Plot a joint plot to understand the relation between Perimeter and Compactness and write your inference.
4. Plot a scatter plot to compare Perimeter and Compactness with different types having different colors (use legend).
5. Plot a box plot to understand the correlation between Compactness and Type.
6. Plot box and strip plots to understand the correlation between Compactness and Type and state your inference.
7. Plot box and strip plots to understand the correlation between Perimeter and Type.
8. Plot violin and strip subplots to understand the correlation between Compactness and Type and state your inference.
9. Plot kernel density estimation plots to understand the correlation between Compactness and Type and state your inference.
10. Plot a pair plot to understand all characteristics with Type being the main parameter and state your inference.
11. Plot a pair plot to understand all characteristics with Type being the main parameter, using KDE instead of a histogram in diagonal subplots.
12. Plot an Andrews curve to display the separability of data according to Type.
13. Plot a bar plot for the given X and Y values.
    - X = [2, 8, 10]
    - Y = [11, 16, 9]
    - X2 = [2, 3, 6]
    - Y2 = [4, 16, 9]

Please follow the instructions above to perform the data visualization tasks using the provided libraries.

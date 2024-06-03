# README

## Table of Contents

- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Outcome](#outcome)
- [Theory](#theory)
  - [Data Visualization](#data-visualization)
  - [Common Python Libraries](#common-python-libraries)
  - [Types of Plots](#types-of-plots)
    - [Scatter Plot](#scatter-plot)
    - [Pair Plot](#pair-plot)
    - [Box Plot](#box-plot)
    - [Violin Plot](#violin-plot)
    - [Joint Plot](#joint-plot)
    - [Bar Chart](#bar-chart)
    - [Line Plot](#line-plot)
- [Tasks](#tasks)

## Aim
### To understand and implement data visualization techniques.

## Prerequisite

- Python Programming
- Pandas Library
- Numpy Library
- Matplotlib
- Seaborn Library

## Outcome
After successful completion of this experiment students will be able to:

1. Read different types of data files (csv, excel, text file etc.)
2. Understand usage of different types of Python libraries for plotting data
3. Plot data using different types of plots

## Theory

### Data Visualization
Data visualization is a form of visual communication. It involves the creation and study of the visual representation of data. It translates the data to a more natural form for the human mind to comprehend and pick out patterns or points of interest.

### Common Python Libraries
Matplotlib and seaborn are among the common libraries for visualizing data in Python. 

- **Matplotlib**: A python library used extensively for the visualization of data.
- **Seaborn**: A python library based on matplotlib. Seaborn provides a high-level interface for drawing attractive and informative statistical graphics.

### Types of Plots

#### Scatter Plot
It is one of the most commonly used plots for simple data visualization. It gives us a representation of where each point in the entire dataset is present with respect to any 2 or 3 features (or columns).

#### Pair Plot
Pair plot will help us create a (n x n) figure where the diagonal plots will be histogram plots of the feature corresponding to that row and rest of the plots are the combination of feature from each row in the y-axis and feature from each column in the x-axis.

#### Box Plot
A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution.

#### Violin Plot
The violin plots can be inferred as a combination of Box plot at the middle and distribution plots (Kernel Density Estimation) on both sides of the data. This can give us the details of distribution like whether the distribution is multimodal, Skewness etc.

#### Joint Plot
Joint plots can do both univariate as well as bivariate analysis. The main plot will give us a bivariate analysis, whereas on the top and right side we will get univariate plots of both the variables that were considered. It makes our job easy by getting both scatter plots for bivariate and Distribution plot for univariate, both in a single plot.

#### Bar Chart
A bar chart or bar graph is a chart that presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

#### Line Plot
A line plot or line chart is a type of chart which displays information as a series of data points called 'markers' connected by straight line segments.

## Tasks

1. Read “seeds.csv” file into a data frame.
2. Explore the dataset by using `head` and `describe`.
3. Find the number of samples per type. Plot a histogram for the count.
4. Plot a scatter plot for Kernel Width vs Length. Write your inference.
5. Plot a Jointplot to understand the relation between Perimeter and Compactness. Write your inference.
6. Plot a Scatter plot to compare Perimeter and Compactness. Different types should have different colors (hint: use legend).
7. Plot a Box plot to understand the correlation between compactness and type.
8. Plot Box & Strip plots to understand the correlation between compactness and type. State your inference.
9. Plot Box & Strip plots to understand the correlation between perimeter and type.
10. Plot Violin and strip subplots to understand the correlation between compactness and type. State your inference.
11. Plot Kernel Density Estimation plots to understand the correlation between compactness and type. State your inference.
12. Plot a pair plot to understand all characteristics with type being the main parameter. State your inference.
13. Plot a pair plot to understand all characteristics with type being the main parameter, with KDE instead of histogram in diagonal subplots.
14. Plot an Andrews curve to display the separability of data according to Type.
15. Plot a bar plot for below X and Y values.

- X = [2, 8, 10], Y = [11, 16, 9]
- X2 = [2, 3, 6], Y2 = [4, 16, 9]

# Natural Language Processing

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Outcome](#outcome)
- [Theory](#theory)
- [References](#references)

## Aim
### Text preprocessing level two operations - Feature engineering of textual data
- To implement label encoding and one hot encoding on textual data.
- To implement Bag of Words (BoW) feature engineering technique on textual data.
- To implement TF-IDF feature engineering technique.
- To analyze and comprehend the effect of various approaches to convert text into vectors.

## Prerequisite
- Python

## Outcome
After successful completion of this experiment, students will be able to understand concepts, significance, and limitations of various feature engineering methods applied on textual data.

## Theory
Representation of a word in appropriate numerical form is called as feature engineering for text. There are various approaches to feature engineering like label encoding, one hot encoding, bag of words, TF-IDF, etc.

### One Hot Encoding
#### Algorithm
- Create a vocabulary from the given corpus.
- Assign binary vector to each word in the vocabulary.

#### Example
After tokenization, punctuation removal, and stop word removal:
['india', 'country', 'occupies', 'greater', 'part', 'south', 'asia', 'capital', 'new', 'delhi']

Vocabulary:
|       | india | country | occupies | greater | part | south | asia | capital | new | delhi |
|-------|-------|---------|----------|---------|------|-------|------|---------|-----|-------|
| india |   1   |    0    |    0     |    0    |  0   |   0   |  0   |    0    |  0  |   0   |
| country |  0  |    1    |    0     |    0    |  0   |   0   |  0   |    0    |  0  |   0   |
| occupies | 0 |    0    |    1     |    0    |  0   |   0   |  0   |    0    |  0  |   0   |
| greater |  0  |    0    |    0     |    1    |  0   |   0   |  0   |    0    |  0  |   0   |
| part |     0  |    0    |    0     |    0    |  1   |   0   |  0   |    0    |  0  |   0   |
| south |    0  |    0    |    0     |    0    |  0   |   1   |  0   |    0    |  0  |   0   |
| asia |     0  |    0    |    0     |    0    |  0   |   0   |  1   |    0    |  0  |   0   |
| capital |  0  |    0    |    0     |    0    |  0   |   0   |  0   |    1    |  0  |   0   |
| new |      0  |    0    |    0     |    0    |  0   |   0   |  0   |    0    |  1  |   0   |
| delhi |    0  |    0    |    0     |    0    |  0   |   0   |  0   |    0    |  0  |   1   |

### Label Encoding
#### Algorithm
- Create a vocabulary from the given corpus.
- Assign a number to each word in the vocabulary.

#### Example
After tokenization, punctuation removal, and stop word removal:
['india', 'country', 'occupies', 'greater', 'part', 'south', 'asia', 'capital', 'new', 'delhi']

After sorting and assigning an index:
{'asia': 1, 'capital': 2, 'country': 3, 'delhi': 4, 'greater': 5, 'india': 6, 'new': 7, 'occupies': 8, 'part': 9, 'south': 10}

Output after label encoding:
|        | india | country | occupies | greater | part | south | asia | capital | new | delhi |
|--------|-------|---------|----------|---------|------|-------|------|---------|-----|-------|
| Sentence1 |   6   |    3    |    8     |    5    |  9   |   10  |   1  |    2    |  7  |   4   |

### Bag of Words (BoW)
A bag-of-words model is a way of extracting features from text for use in modeling, such as with machine learning algorithms. It involves creating a vocabulary of known words and measuring the presence of these words in the document, disregarding word order.

### TF-IDF (Term Frequency-Inverse Document Frequency)
TF-IDF is another feature engineering technique that weighs the importance of words in a document relative to the entire corpus.

---

This README provides a comprehensive overview of text preprocessing operations in NLP, detailing various feature engineering techniques without including any code snippets.

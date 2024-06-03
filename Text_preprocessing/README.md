# Natural Language Processing

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Outcome](#outcome)
- [Theory](#theory)
- [Task to be Completed in PART B](#task-to-be-completed-in-part-b)

## Aim
### Text Preprocessing level one operations
- To implement operations such as change of case, sentence tokenization, word tokenization, stop word removal, punctuation mark removal, stemming, lemmatization, Parts of Speech (PoS) tagging using NLTK (Natural Language Tool Kit) platform
- To implement tokenization without using built-in function of NLTK
- To comprehend the difference between stemming and lemmatization
- To count frequency of each word in the given document

## Prerequisite
- Python

## Outcome
After successful completion of this experiment students will be able to understand basic concepts of text processing.

## Theory
Natural Language Processing (NLP) is a branch of Data Science which deals with text data. Apart from numerical data, text data is available extensively and is used to analyze and solve business problems. However, before using the data for analysis or prediction, processing the data is important.

To prepare the text data for model building, text preprocessing is the very first step in NLP projects. Some of the preprocessing steps include:
- Removing punctuations like . , ! $( ) * % @
- Removing URLs
- Removing stop words
- Lowercasing
- Tokenization
- Stemming
- Lemmatization
- Part-of-Speech Tagging

### Steps to clean the data

- **Punctuation Removal:** In this step, all the punctuations from the text are removed. The `string` library in Python contains some pre-defined lists of punctuations.
  
- **Lowering the Text:** It is a common preprocessing step where the text is converted into the same case, preferably lower case. However, lowercasing can lead to loss of information in some NLP problems.

- **Tokenization:** The text is split into smaller units. Sentence tokenization or word tokenization can be used based on the problem statement.

- **Stop Word Removal:** Stop words are commonly used words that carry less or no meaning. NLTK library provides a list of stop words for the English language.

- **Stemming:** It reduces words to their root/base form. However, stemming may result in words losing their meaning or not being reduced to proper English words.

- **Lemmatization:** It reduces words to their base form while preserving their meaning using a pre-defined dictionary.

- **Part-of-Speech Tagging:** Tags are assigned to words defining their main context, functions, and usage in a sentence.

## Task to be Completed in PART B
### A.5 Task
- To implement operations such as change of case, sentence tokenization, word tokenization, stop word removal, punctuation mark removal, stemming, lemmatization, Parts of Speech (PoS) tagging using NLTK (Natural Language Tool Kit) platform
- To implement tokenization without using built-in function of NLTK
- To comprehend the difference between stemming and lemmatization
- To count frequency of each word in the given document

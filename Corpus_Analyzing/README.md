# Natural Language Processing

## Table of Contents
- [Aim](#aim)
- [Prerequisite](#prerequisite)
- [Outcome](#outcome)
- [Theory](#theory)
- [Task to be completed in PART B](#task-to-be-completed-in-part-b)
- [References](#references)

## Aim
### Analyzing Guttenberg and Brown corpus using Python
- Working with corpus file list.
- Working with file contents.
- Visualization.

## Prerequisite
- Python

## Outcome
After successful completion of this experiment, students will be able to:
1. Familiarize with Guttenberg and Brown Corpus.
2. Acquaint with methods and techniques to access, understand, and analyze various texts of the corpus.

## Theory
### Guttenberg Corpus
Project Guttenberg is a library of over 70,000 free ebooks. NLTK includes a small selection of texts from the Project Gutenberg electronic text archive. For more details, visit [Project Guttenberg](https://www.gutenberg.org/).

### NLTK Operations on Gutenberg Corpus
To see file identifiers in NLTK Gutenberg corpus:
```python
from nltk.corpus import gutenberg
gutenberg.fileids()
```

To access words in 'Emma' by Jane Austen and apply concordance:
```python
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance("surprize")
```

### Brown Corpus
The NLTK Brown Corpus is a general corpus of present-day American English, comprising 500 samples from a wide range of sources.
```python
from nltk.corpus import brown
files = brown.fileids()
brown.categories()
```

To access words from the 'news' category in Brown Corpus:
```python
brown.words(categories='news')
```

### Accessing Text from Web and Local Disk
For more information on accessing text from web and local disk, refer to:
- [Chapter 3 of NLTK Book](https://www.nltk.org/book/ch03.html)

## Task to be completed in PART B
### Task
- To access Gutenberg corpus from NLTK, list all the texts available.
- To write a function to analyze each text in the corpus using `raw()`, `sents()`, `words()` functions from NLTK.
- To access Brown corpus from NLTK and list all the available texts.
- To write a function to compare different genres (categories) in Brown corpus.
- To access text from the web and perform various operations.
- To access HTML documents and perform operations on HTML text.
- To read text from a local file on disk and perform tokenization.

## References
1. [Chapter 1 of NLTK Book](https://www.nltk.org/book/ch01.html)
2. [Chapter 2 of NLTK Book](https://www.nltk.org/book/ch02.html)
3. [Chapter 3 of NLTK Book](https://www.nltk.org/book/ch03.html)

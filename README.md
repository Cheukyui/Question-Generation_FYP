# GENERATING SEMANTICALLY SIMILAR PERMUTATIONS OF QUESTIONS

#### Table of Contents  
[Introduction](#introduction)  
[Installation](#installation)  
[Usage](#usage) 

## Introduction
This repository provides a command line script written in Python for generating permutations of questions from an input English question automatically. The generated questions can be used in training of automated question answering models as augmentation of training datasets. This augmentation technique is especially useful when training datasets are small and limited. 

This Question Generation (QG) system involves 2 approaches. The descriptions of each question generation approach are given below:

- **Combination of machine translation applications question generator**. Given an input question, this question generator will generate permutations of questions by translating the input question utilising a combination of machine translation applications into Chinese language and translating the sentence back to English language.
- **Permutation of translated Chinese sentence question generator**. Given an input question, this question generator will generate permutations of questions by permutation of the Chinese translated question and translating the different permutations back to English language.

## Installation
### Step 1: Clone the repository
```
git clone --recursive https://github.com/Cheukyui/Question-Generation_FYP
cd Question-Generation_FYP
```

### Step 2: Install the dependencies
Create a virtual environment
```
python -m virtualenv env
source env/bin/activate
```

Install the required modules using the following code
```
pip install -r requirements.txt 
```

## Usage

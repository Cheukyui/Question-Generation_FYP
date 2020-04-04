# GENERATING SEMANTICALLY SIMILAR PERMUTATIONS OF QUESTIONS

#### Table of Contents  
[Introduction](#introduction)  
[Installation](#installation)  
[Usage](#usage) 

## Introduction
This repository provides a command line script written in Python for generating permutations of questions from an input English question automatically. The generated questions can be used in training of automated question answering models as augmentation of training datasets. This augmentation technique is especially useful when training datasets are small and limited. 

This Question Generation (QG) system involves 2 approaches. The descriptions of each question generation approach are given below:

- **Combination of machine translation applications question generator**. Given an input question, this question generator will generate permutations of questions by translating the input question utilising a combination of machine translation applications into Chinese language and translating the sentence back to English language.
- **Permutation of translated Chinese sentence question generator**. Given an input question, this question generator will generate permutations of questions by permutation of the Chinese translated question and translating the different permutations back to English language. In addition to taking an English question as an input, there will be another python script that allows users to read a text file of English questions called: "question_bank.txt" and returning a text file of generated questions to the user called: "generate.txt".

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
env\Scripts\activate
```

Install the required modules for running the python script
```
pip install -r requirements.txt
```

## Usage
### Combination of machine translation applications question generator


### Permutation of translated Chinese sentence question generator
Run the python script
```
python Eng_chi_permute.py
```
After running the above code, the user will be prompted to input an English question like below:
```
Please input an English question:
```
Sample Output:
```
```

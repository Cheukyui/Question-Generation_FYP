# GENERATING SEMANTICALLY SIMILAR PERMUTATIONS OF QUESTIONS

#### Table of Contents  
[Introduction](#introduction)  
[Installation](#installation)  
[Usage](#usage) 

## Introduction
This repository provides a command line script written in Python for generating permutations of questions from an input English question automatically. The generated questions can be used in training of automated question answering models as augmentation of training datasets. This augmentation technique is especially useful when training datasets are small and limited. 

This Question Generation (QG) system involves 2 approaches. The descriptions of each question generation approach are given below:

- **Combination of machine translation applications question generator**. Given an input question, this question generator will generate permutations of questions by translating the input question utilising a combination of machine translation applications into Chinese language and translating the sentence back to English language.
- **Permutation of translated Chinese sentence question generator**. Given an input question, this question generator will generate permutations of questions by permutation of the Chinese translated question and translating the different permutations back to English language. This python script will return an unique set of English questions with no duplicates. In addition to taking an English question as an input, there will be another python script that allows users to read a text file of English questions where users just have to input the name of the text file filled with English questions and returning a text file of generated questions to the user called: "generate.txt".

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

Install the required modules for running the python scripts
```
pip install -r requirements.txt
```

## Usage
### Combination of machine translation applications question generator


### Permutation of translated Chinese sentence question generator
#### Input: Single English Question
Run the python script
```
python Eng_chi_permute.py
```

After running the above code, the user will be prompted to input an English question like below:
```
Please input an English question:
```

Sample Input:
```
How is the birth order determined
```

Sample Output:
```
how is it confirm birth order
how to determine the order of birth
how to determine born order
how is it determine born order
how to determine birth order
how is it determine birth order
```

Another function within this python script is available if the user wants to extract the most dissimilar generated questions compared to the input English question. This function can be activated by calling the function like this below:
```
similarity_list(eng_qns, unique_list(seg_sentence))
```

#### Input: Text File of English Questions
Run the python script
```
python Eng_chi_text_file.py
```

After running the above code, the user will be prompted to input the name of the text file like below:
```
Please input name of text file:
```

Sample Input:
```
question_bank.txt
```

Sample Contents inside the Text File:
```
What is baby bonus
How to determine birth order
```

Sample Output:
```
What is a baby bonus
What is a baby bonus
what is Baby bonus
what is baby bonus
what Is a baby bonus
what Is a baby bonus
what Yes Baby bonus
what Yes baby bonus


How to determine the order of birth
How to determine birth order
How to determine Birth order
How to determine Born order
how is it Determine birth order
how is it Confirm birth order
how is it determine Birth order
how is it determine Born order
```
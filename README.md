# Genesis AI/NLP Team Project
In this project we do Kaggle competition: <br>
[Text Normalization Challenge](https://www.kaggle.com/c/text-normalization-challenge-english-language/data) <br>
Download the datasets: <br>
[en_train.csv](https://www.kaggle.com/c/text-normalization-challenge-english-language/download/en_train.csv), <br>
[en_test_2.csv](https://www.kaggle.com/c/text-normalization-challenge-english-language/download/en_test_2.csv), <br>
[en_sample_submission_2.csv](https://www.kaggle.com/c/text-normalization-challenge-english-language/download/en_sample_submission_2.csv)

## Brief Introduction
### The competition
to be added...
### NLP
to be added...
### Tensorflow
to be added...


# Meeting Proceedings
## 2018.10.14 Minutes of Meeting
Attendence: Simon, William, Steven, Tianyi
1. Decide to do competiion on Kaggle: https://www.kaggle.com/c/text-normalization-challenge-english-language/data
2. Roles: </br>
  William: Documentation on Github / Minutes of Meeting </br>
  Steven, Simon: Come up with a model to deal with texts (words). </br>
  Tianyi, William: Post some brief descriptions on NLP, Tensorflow. </br>
  
3. We will run the model on Steven/Simon's computer
4. We use python
5. Next Meeting: 20th Oct Sat 4 p.m. 



## 2018.10.20 Minutes of Meeting
Attendence: Simon, William, Steven, Tianyi
1. **Temporary goal:** <br>
   To increase the accuracy in the test data provided in kaggle's english text normalization competition (en_test_2.csv). <br> 
   The current accuracy of said data set is roughly 92%: 
   ![Round 0](https://github.com/astro1boy/AI_Team_Project/blob/master/Scores/Round%200.png?raw=true)<br>
   *(This result is achieved by uploading the testset with 'after' column exactly identical to 'before' column)*
2. Data types that we want to focus to change for now : Integers and date. So if the data is '2', change it to 'two'. <br> 
3. One proposed method to identify whether character or set of characters needs to be changed: <br>
    > 1. Create a vocabulary <br> 
    > 2. Assign simple distinct values to each character in the vocabulary in order to identify each character <br> 
    
    **EXAMPLE:** <br>
    For a vocab containing 6 keys: **a b c . * 2** <br>

    | 6 | 6 |   |   |   |   |   |
    | - |:-:|:-:|:-:|:-:|:-:|:-:|
    | a | 1 | 0 | 0 | 0 | 0 | 0 |
    | b | 0 | 1 | 0 | 0 | 0 | 0 |
    | c | 0 | 0 | 1 | 0 | 0 | 0 | 
    | . | 0 | 0 | 0 | 1 | 0 | 0 |     
    | * | 0 | 0 | 0 | 0 | 1 | 0 |     
    | 2 | 0 | 0 | 0 | 0 | 0 | 1 |

    Each character is assigned values
   > Possible Alternative way: Using the ASCII code for to give each characters values —— by Steven <br> 

5. Figuring out if a character is a number or a text or any other data types. <br> 
    >proposal #1 -> giving datas that needs to be changed (like numbers, dates, etc) a pattern in their values.  
    >proposal #2 -> Make three arrays : alphabets, numbers and punctuations. Then input in these arrays values of each character, alphabet value into alphabet array, so on. Then when the program is checking a word, compare the character with the elements of the arrays to know the character's data types. 
                                                           
6. Summary of Steven's alternative method on identifying which characters need to change : <br> 
        - Have each word (instead of character) assigned different values <br> 
        - put part of the values into arrays <br> 
        - Let program learn the patterns <br> 
                                 
7. **Tasks of this week:** <br>
        - William: Build the vocabulary with [en_train.csv](https://www.kaggle.com/c/text-normalization-challenge-english-language/download/en_train.csv) using python, exactly like point 3 above <br>
        - Steven: Find a baseline model for the task of point 4 above <br>
        - Tianyi: Pending <br>
        - Simon: Ready to help when necessary, upload files needed onto github <br>
    > Tips for William
    > 1. reading in all texts in 'before' column from the file. For reading operations, try [csv](https://docs.python.org/3.6/library/csv.html) or [pandas.read_csv](https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/)
    > 2. spliting all characters (space should be as well regarded as a char), try list(string)
    > 3. removing duplications, try "set(list)"
    > 4. assign for each distinct char in the set, a vector, with all 0s except one place (as discussed).
    > 5. write the vocabulary along with their vectors, into a file with format as discussed. You can find the answer either by googling or checking the python documentation. 
    > <br> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; —— by Simon


## 2018.11.02 Minutes of Meeting
Attendence: Simon, William, Steven, Kiven (New Member, Welcome!)
1. Decided to tackle the project with Machine Learning. <br>
2. Steven will present his Model next time. <br>
3. Individual programming using python and pandas packages. Trying to create dictionary. <br>
4. We found a lot of special characters included in the training set, like chinese chars, japaness chars, strange chars, etc. And they mainly exists in the "VERBATIM" class. When the VERBATIM characters are removed, the number of special characters shrinked from 3000+ to 112: ![pic](https://github.com/astro1boy/AI_Team_Project/blob/master/_cachepic/removing_VERBATIM.png) <br> 
It is decided that the dictionary will be built without the VERBATIM class characters and every character not included in the dictionary will be treated as special character by the program and be given special values.
6. From the last meeting it was decided that each character are going to be given values such as 00010000 or 10000000, <br>
Simon suggested that each word in the test data is given a matrix of said values. For example, Apple would be : <br>
        | 1 | 0 | 0 | 0 | 0 | 0 |<br>
        | 0 | 1 | 0 | 0 | 0 | 0 |<br>
        | 0 | 0 | 1 | 0 | 0 | 0 |<br>
        | 0 | 0 | 0 | 1 | 0 | 0 |<br>
        | 0 | 0 | 0 | 0 | 1 | 0 |     
        | 0 | 0 | 0 | 0 | 0 | 1 |<br>         Matrix for Apple<br>
And each words/cell in the test data will have matrix like this then said matrices will later be used for Machine learning so that the computer can recognize its pattern.<br>

7. **Progresses of this week:** <br>
  > a. Dictionary built, see file: dict01 *(Good to have a Notepad++ to directly open it)*<br>
  &emsp;   1. the begining of first line is blank, which means the vector value to <space>. <br>
  &emsp;   2. there is a char called '<UNKNOWN_CHAR>', which all chars not appeared should go to this vector value. <br>
  > b. one-hot.py -> codes to get dict01<br>
  > c. viewingData.py -> codes to travel into the dataset
    
8. **Tasks of this week:** <br>
        - **Kiven**: Get the one-hot matrix for each cell in 'before' and 'after' column using the dictionary provided, as well its label(class). And store them into a numpy file. <br>
        - **William**: <br>
        a. Try to post some descriptions/introductions (approximately 200 words) of what is the competition doing, how are we doing(preliminary), why are we doing like this(you can try google some answers). <br>
        b. Try running the python scripts written for this weeks' task (one-hot & dataViewing), so to have an understanding of python & our competition. <br>
        *c. Just for information, William can try to learn some basics of ML if he wanted to, [Machine Learning on Coursera for FREE!](https://www.coursera.org/learn/machine-learning) could be a good starting point* <br>
        - **Steven**: Run the XGBoost model, which needs no dictionary, and see the accuracy <br>
        - **Simon**: Ready to help when necessary <br>

## Useful Links
[Markdown Cheetsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) <br>
One key finding: Github Markdown allows multiple selecting & multi-cursor editing！！！ (just like sublime text)



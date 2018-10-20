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
1. Decide to do competiion on Kaggle: https://www.kaggle.com/c/text-normalization-challenge-english-language/data
2. Roles: </br>
  William: Documentation on Github / Minutes of Meeting </br>
  Steven, Simon: Come up with a model to deal with texts (words). </br>
  Tianyi, William: Post some brief descriptions on NLP, Tensorflow. </br>
  
3. We will run the model on Steven/Simon's computer
4. We use python
5. Next Meeting: 20th Oct Sat 4 p.m. 



## 2018.10.20 Minutes of Meeting
1. **Temporary goal:** <br>
   To increase the accuracy in the test data provided in kaggle's english text normalization competition (en_test_2.csv). <br> 
   The current accuracy of said data set is roughly 92%. <br>
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
   > Possible Alternative way: Using the ASCII code for to give each characters values <br> 

5. Figuring out if a character is a number or a text or any other data types. <br> 
    >proposal #1 -> giving datas that needs to be changed (like numbers, dates, etc) a pattern in their values.  
    >proposal #2 -> Make three arrays : alphabets, numbers and punctuations. Then input in these arrays values of each character, alphabet value into alphabet array, so on. Then when the program is checking a word, compare the character with the elements of the arrays to know the character's data types. 
                                                           
6. Summary of Steven's alternative method on identifying which characters need to change : <br> 
        - Have each word (instead of character) assigned different values <br> 
        - put part of the values into arrays <br> 
        - Let program learn the patterns <br> 
                                 
7. **Jobs of this week:** <br>
        - William: Build the vocabulary with [en_train.csv](https://www.kaggle.com/c/text-normalization-challenge-english-language/download/en_train.csv) using python, exactly like point 3 above <br>
        - Steven: Find a baseline model for the task of point 4 above <br>
        - Tianyi: Pending <br>
        - Simon: Ready to help when necessary, upload files needed onto github <br>
    > Tips for William
    > 1. reading in all texts in 'before' column from the file. For reading operations, try [csv](https://docs.python.org/3.6/library/csv.html) or [pandas.read_csv](https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/)
    > 2. spliting all characters (space should be as well regarded as a char), try list(string)
    > 3. removing duplications, try "set(list)"
    > 4. assign for each distinct char in the set, a vector, with all 0s except one place (as discussed).
    > 5. write the vocabulary along with their vectors, into a file with format as discussed. Try Google. 
    > <br> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; —— by Simon


## Useful Links
[Markdown Cheetsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) <br>
One key finding: Github Markdown allows multiple selecting & multi-cursor editing！！！ (just like sublime text)

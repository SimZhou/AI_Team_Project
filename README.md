# Genesis AI/NLP Team Project
For Kaggle competition: https://www.kaggle.com/c/text-normalization-challenge-english-language/data

## Brief Introduction
### The competition
to be added...
### NLP
to be added...
### Tensorflow
to be added...



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
1. Temporary goal : To increase the accuracy in the test data provided in kaggle's english text normalization competition                                   (en_test_2.csv).</br> 
                    The current accuracy of said data set is roughly 92%.</br> 
2. Data types that we want to focus to change for now : Integers and date. So if the data is '2', change it to 'two'.</br> 
3. One proposed method to identify whether character or set of characters needs to be changed : </br> 
                                - Create a vocabulary</br> 
                                - Assign simple distinct values to each character in the vocabulary in order to identify each character</br> 
                                        EXAMPLE : abx.*2</br> 
                                        a -> 1 0 0 0 0 0</br> 
                                        b -> 0 1 0 0 0 0</br> 
                                        c -> 0 0 1 0 0 0</br> 
                                        . -> 0 0 0 1 0 0</br> 
                                        * -> 0 0 0 0 1 0</br> 
                                        2 -> 0 0 0 0 0 1</br> 
                                        each character is assigned values</br> </br> 
                                 - Possible Alternative way: Using the ASCII code for to give each characters values</br> 
                                 - Figuring out if a character is a number or a text or any other data types.</br> 
                                         &emsp;  - proposal #1 -> giving datas that needs to be changed(like numbers, dates, etc)
                                                           a pattern in their values.</br> 
                                         &emsp;  - proposal #2 -> Make three arrays : alphabets, numbers and punctuations. Then input in these
                                                           arrays values of each character, alphabet value into alphabet array, so on.
                                                           Then when the program is checking a word, compare the character with the
                                                           elements of the arrays to know the character's data types. </br> 
4. Summary of Steven's alternative method on identifying which characters need to change :</br> 
                               &emsp;   - Have each word(not character) assigned different values</br> 
                               &emsp;   - put part of the values into arrays</br> 
                               &emsp;   - Let program learn the patterns</br> 
                                 


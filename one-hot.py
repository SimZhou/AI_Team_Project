import pandas as pd

# defining the path
path = 'D:\\Yihua\\KaggleCompetition\\textNormalization\\data\\en_train.csv'

# Read csv into pandas
data_train = pd.read_csv(path)

# Get the data without 'VERBATIM' class
data_02 = data_train[data_train['class'] != 'VERBATIM']

# dump words in 'before' and 'after' columns into a variable 
dump = []
for cell_before in data_02.iloc[:,3]:
    dump.append(cell_before)

for cell_after in data_02.iloc[:,4]:
    dump.append(cell_after)

# change all elements into str
dump_str = []
for ele in dump:
    dump_str.append(str(ele))

# get the characters in those words
chars = []
for cell in dump_str:
    chars.extend(list(cell))

# build the character dict (This is manual way), for simple way just use list(set(chars))
i = 0
chars_dict = []
for ele in chars:
    if ele not in chars_dict:
        chars_dict.append(ele)

# preparing to get the one-hot
import numpy as np
one_hot = np.identity(len(chars_dict) + 1, dtype = np.int) # to + 1 means I want to assign a vector to <UNKNOWN_CHAR> too.  

# Add the <UNKNOWN_CHAR> and then sort the list
chars_dict.append('<UNKNOWN_CHAR>')
chars_dict = sorted(chars_dict)

# Get values ready for writing into the file
one_hot_to_write = []
for index in range(len(chars_dict)): 
    one_hot_to_write.append(chars_dict[index] + " " + " ".join(str(x) for x in list(one_hot[index])) + '\n')

# Write into the file
with open('D:\\Yihua\\KaggleCompetition\\textNormalization\\dict01', "w", encoding = 'utf-8') as f: 
    line = f.writelines(one_hot_to_write)

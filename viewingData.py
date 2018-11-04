import pandas as pd

# defining the path
path = 'D:\\Yihua\\KaggleCompetition\\textNormalization\\data\\en_train.csv'

# Read csv into pandas
data_train = pd.read_csv(path)

# See how many classes are there in the data: 
set([i for i in data_train['class']]) # returns: {'MEASURE', 'TIME', 'DIGIT', 'ADDRESS', 'ORDINAL', 'DATE', 'PUNCT', 'ELECTRONIC', 'TELEPHONE', 'VERBATIM', 'FRACTION', 'CARDINAL', 'LETTERS', 'MONEY', 'DECIMAL', 'PLAIN'}

# See those data in each class
data_train_MEASURE = data_train[data_train['class'] == 'MEASURE']
data_train_TIME = data_train[data_train['class'] == 'TIME']
data_train_DIGIT = data_train[data_train['class'] == 'DIGIT']
data_train_ADDRESS = data_train[data_train['class'] == 'ADDRESS']
data_train_ORDINAL = data_train[data_train['class'] == 'ORDINAL']
data_train_DATE = data_train[data_train['class'] == 'DATE']
data_train_PUNCT = data_train[data_train['class'] == 'PUNCT']
data_train_ELECTRONIC = data_train[data_train['class'] == 'ELECTRONIC']
data_train_TELEPHONE = data_train[data_train['class'] == 'TELEPHONE']
data_train_VERBATIM = data_train[data_train['class'] == 'VERBATIM']
data_train_FRACTION = data_train[data_train['class'] == 'FRACTION']
data_train_CARDINAL = data_train[data_train['class'] == 'CARDINAL']
data_train_LETTERS = data_train[data_train['class'] == 'LETTERS']
data_train_MONEY = data_train[data_train['class'] == 'MONEY']
data_train_DECIMAL = data_train[data_train['class'] == 'DECIMAL']
data_train_PLAIN = data_train[data_train['class'] == 'PLAIN']

# Don't run following lines at a time, if you don't want your system crash!!!
data_train_MEASURE
data_train_TIME
data_train_DIGIT
data_train_ADDRESS
data_train_ORDINAL
data_train_DATE
data_train_PUNCT
data_train_ELECTRONIC
data_train_TELEPHONE
data_train_VERBATIM
data_train_FRACTION
data_train_CARDINAL
data_train_LETTERS
data_train_MONEY
data_train_DECIMAL
data_train_PLAIN

# writing some dataframes into file, to have a better view: 
data_train_VERBATIM.to_csv('D:\\Yihua\\KaggleCompetition\\textNormalization\\data\\VERBATIM.csv') # Although it's a csv but it is better to be opened with Notepad++

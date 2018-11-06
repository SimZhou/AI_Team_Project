'''
This file saves the 'before', 'after' and 'class' to files as one-hots
- Will write more than 30gb of data to nearly 200 files
This version directly saves one-hot matrices (vectors)
- Due to the irregularity of the one-hots of words,
the dtype of the 'before' and 'after' is object (numpy arrays)
'''

import numpy as np
import pandas as pd
import sys
import klepto

def flush(*args):
	# this function clears current line of the console and write something,
	# which helps tracking the progress
	CLEAR = " " * 100 + "\r"
	sys.stdout.write(CLEAR)
	for a in args:
		sys.stdout.write(str(a))  # write() only accepts string
	sys.stdout.flush()


def _gen_test_data():
	pass
	
	
def _get_csv_record(name, data=None) -> list:
	dump = []
	if name == "before":
		for cell in data.iloc[:, 3]:
			dump.append(cell)
	elif name == "after":
		for cell in data.iloc[:, 4]:
			dump.append(cell)
	elif name == "tag":
		for cell in data.iloc[:, 2]:
			dump.append(cell)
	else:
		raise(AttributeError("cannot find such column"))
	return dump


def _get_dict():  # deprecated
	with open("dict01", encoding='utf-8') as f:
		char_dict = {}
		for line in f.readlines():
			if not line.startswith(" "):  # in case of space as a character
				token, numstr = line.split(' ', 1)
			else:
				token = " "
				_, numstr = line.split('  ', 1)
			one_hot = np.mat(numstr).T
			char_dict[token] = one_hot
	return char_dict


def _get_index_dict():
	with open("dict01", encoding='utf-8') as f:
		char_dict = {}
		for line in f.readlines():
			if not line.startswith(" "):  # in case of space as a character
				token, numstr = line.split(' ', 1)
			else:
				token = " "
				_, numstr = line.split('  ', 1)
			idx = numstr.split(' ').index('1')
			char_dict[token] = idx
	return char_dict


def _to_obj_ndarray(data: list) ->np.ndarray:
	# this helper function converts a 1D list of objects
	# into an ndarray, to avoid being broadcasted
	print("Converting data for writing ... ")
	output = np.empty((len(data),), dtype=object)
	# thanks to slicing, for-loops are not needed here
	output[:] = data
	print("converted")
	return output


def transform(data, cdict) ->list:
	'''
	WARNING: no memory optimization yet
	memory consumption up to 15g
	still runs well, though
	'''
	output = []
	i = 0  # counter
	length = len(data)
	percent = length // 100
	for w in data:
		i += 1
		if i % percent == 0:
			flush(i//percent, '% done')
		twod_vec = None
		for c in str(w):  # in case of some "nan" problem
			cvec = cdict[c]
			if twod_vec is None:
				twod_vec = cvec
			else:
				twod_vec = np.concatenate((twod_vec, cvec), axis=1)
		output.append(twod_vec)
	print("\nCompleted")
	# the dtype has to be clarified so that the constructing function
	# will not try to broadcast it
	return output


def _to_one_hot(idx, dim):
	# This helper function tranforms an index
	# into a ROW one-hot vector
	return np.eye(dim)[idx].T


def transform_tags(data) -> (dict, np.ndarray):
	# this function returns
	# - the class-to-one-hot dictionary
	# - a writable ndarray of one-hot ROW vectors
	# to retrieve dictionary values, invoke
	# np.load("file").items().get("key")

	print("converting tags ... ")
	types = sorted(set(data))
	dim = len(types)
	idx_of = {t: idx for idx, t in enumerate(types)}  # enumerate -> (number, item)
	output = [_to_one_hot(idx_of[i], dim) for i in data]

	print("Done")
	return idx_of, np.array(output)


def _save_to_chunks(addr_plus_name_no_surfix, data, chunk_size=100_000):
	end = len(data)
	name = addr_plus_name_no_surfix
	st = 0
	ed = chunk_size
	counter = 1
	while st<=end:
		np.save(name+str(counter), data[st:ed])
		counter += 1
		flush("saved ", counter, " file(s)")
		st += chunk_size
		ed = ed + chunk_size
		if ed>end:
			ed = end


if __name__ == "__main__":
	print("Reading file...")
	data_train = pd.read_csv("data/en_train.csv")
	data_02 = data_train[data_train['class'] != 'VERBATIM']

	print("Processing...")
	before = _get_csv_record("before", data=data_02)
	after = _get_csv_record("after", data=data_02)
	tag = _get_csv_record("tag", data=data_02)

	print("Reading dict...")
	cdict = _get_dict()

	print("Transforming and writing 'before' to file")
	output = transform(before, cdict)
	to_write = _to_obj_ndarray(output)
	del output, data_train, data_02  # in case the memory dries up
	print("data to be written: ", sys.getsizeof(to_write), " bytes")
	_save_to_chunks("data/before", to_write)
	del to_write

	print("Transforming and writing 'after' to file")
	output = transform(after, cdict)
	to_write = _to_obj_ndarray(output)
	del output
	print("data to be written: ", len(to_write), " bytes")
	_save_to_chunks("data/after", to_write)
	print("'after' saved")
	del to_write

	print("Transforming 'tags' ...")
	tag_dict, output = transform_tags(tag)
	print("writing ...")
	np.save("data/tagdict", tag_dict)
	np.save('data/tags', output)

	print("ALL DONE!")

'''
After testing word_to_2d_onehot.py,
considering too much resources it consumes,
I added this file
(Kiven, 181106)
'''


import numpy as np
import pandas as pd
import sys


def flush(*args):
	# this function clears current line of the console and write something,
	# which helps tracking the progress
	CLEAR = " " * 100 + "\r"
	sys.stdout.write(CLEAR)
	for a in args:
		sys.stdout.write(str(a))  # write() only accepts string
	sys.stdout.flush()
	
	
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


def _get_dict():
	with open("dict01", encoding='utf-8') as f:
		char_dict = {}
		for line in f.readlines():
			if not line.startswith(" "):  # in case of space as a character
				token, numstr = line.split(' ', 1)
			else:
				token = " "
				_, numstr = line.split('  ', 1)
			try:
				idx = numstr.split(' ').index('1')
			except:
				idx = len(numstr.split(' '))-1
			char_dict[token] = idx
	print(char_dict)
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
		vec = None
		for c in str(w):  # in case of some "nan" problem
			index = cdict[c]
			if vec is None:
				vec = np.array(index)
			else:
				vec = np.append(vec, index)
		output.append(vec)

	print("\nCompleted")
	# the dtype has to be clarified so that the constructing function
	# will not try to broadcast it
	return output


def transform_tags(data) -> (dict, np.ndarray):
	# this function returns
	# - the class-to-one-hot dictionary
	# - a writable ndarray of indices of the classes
	# to retrieve dictionary values, invoke
	# np.load("file").items().get("key")

	print("converting tags ... ")
	types = sorted(set(data))
	idx_of = {t: idx for idx, t in enumerate(types)}  # enumerate -> (number, item)
	output = [idx_of[i] for i in data]

	print("Done")
	return idx_of, np.array(output)


def _save_to_chunks(addr_plus_name_no_surfix, data, chunk_size=1_000_000):
	end = len(data)
	name = addr_plus_name_no_surfix
	st = 0
	ed = chunk_size
	counter = 0
	while st < end:
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
	_save_to_chunks("data/before", to_write)
	del to_write

	print("\nTransforming and writing 'after' to file")
	output = transform(after, cdict)
	to_write = _to_obj_ndarray(output)
	del output
	_save_to_chunks("data/after", to_write)
	print("\n'after' saved")
	del to_write

	print("Transforming 'tags' ...")
	tag_dict, output = transform_tags(tag)
	print("writing ...")
	np.save("data/tagdict", tag_dict)
	np.save('data/tags', output)

	print("ALL DONE!")

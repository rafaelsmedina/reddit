import matplotlib.pyplot as plt
import numpy as np
import math

datasets = ['german', 'english', 'spanish', 'french']
#datasets = ['english']


for item in datasets:

	filename_in = item + '_data/' + item + '_in_degree'
	filename_out = item + '_data/' + item + '_out_degree'

	fread = open(filename_in, 'r')
	in_degree = fread.readlines()
	in_values = {}

	for i in in_degree:
		in_values[i.split(':')[0].replace(' ', '').replace(',', '')] = int(i.split(':')[1].replace(' ', '').replace(',', ''))

	fread = open(filename_out, 'r')
	out_degree = fread.readlines()
	out_values = {}

	for i in out_degree:
		out_values[i.split(':')[0].replace(' ', '').replace(',', '')] = int(i.split(':')[1].replace(' ', '').replace(',', ''))

	tuples = {}
	for i in in_values:
		if (in_values[i], out_values[i]) in tuples:
			tuples[(in_values[i], out_values[i])] = tuples[(in_values[i], out_values[i])] + 1
		else:
			tuples[(in_values[i], out_values[i])] = 1

	file = open(item + '_in_out_frequency', 'a+')
	print>>file, 'in, out, frequency'

	for i in tuples:
		print>>file, i[0], ",", i[1], ",", tuples[i]
	file.close()

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
	in_values = []
	in_names = []

	for i in in_degree:
		in_values.append(math.log(float(i.split(':')[1].replace(' ', '').replace(',', ''))+1, 10))
		in_names.append(i.split(':')[0].replace(' ', '').replace(',', ''))

	fread = open(filename_out, 'r')
	out_degree = fread.readlines()
	out_values = []
	out_names = []

	for i in out_degree:
		out_values.append(math.log(float(i.split(':')[1].replace(' ', '').replace(',', ''))+1, 10))
		out_names.append(i.split(':')[0].replace(' ', '').replace(',', ''))

	
	print in_values
	row_labels = list(set(in_values))
	column_labels = list(set(out_values))
	
	data = []
	for i in range(0, len(row_labels)):
		aux = []
		for j in range(0, len(column_labels)):
			aux.append(0)
		data.append(aux)

	for i in range(0, len(in_values)):
		row = row_labels.index(in_values[i])
		column = column_labels.index(out_values[i])

		data[row][column] = data[row][column] + 1

	
	data = np.array(data)	

	fig, ax = plt.subplots()
	heatmap = ax.pcolor(data)

	# put the major ticks at the middle of each cell, notice "reverse" use of dimension
	ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)
	ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)


	ax.set_xticklabels(column_labels, minor=False)
	ax.set_yticklabels(row_labels, minor=False)
	plt.title(item.title() + " Comments Heatmap")
	plt.xlabel("Comments made by user")
	plt.ylabel("Replies received by user")
	plt.show()
import statistics


datasets = ['german', 'english', 'spanish', 'french']

for item in datasets:

	filename = item + '_data/' + item + '_post_activity'
	file = open(filename, 'r')
	lines = file.readlines()

	values = []

	if len(lines) == 1:
			lines = lines[0].replace('{', '').replace('}', '').split(',')
			
	for line in lines:
		values.append(float(line.split(':')[1].replace(',', '')))

	print item
	print statistics.median(values), 'median'
	print statistics.mean(values), 'mean'
	print statistics.stdev(values), 'std'
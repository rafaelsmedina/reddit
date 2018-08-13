import networkx as nx

datasets = ['german']

def load_flairs():
	for lang in datasets:
		g = nx.read_gpickle('y_data/threads/nx_' + lang + '_tree')

		flairs = {}

		for item in g.nodes():
			if 'author_flair' in g.node[item] and g.node[item]['author_flair'] != None:
				flairs[item] = g.node[item]['author_flair']

		return flairs

def arrange_flairs(input_flairs):
	german_levels = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'beginner', 'intermediate', 'advanced', 'native']
	flairs = {}
	names = {}

	for flair in input_flairs:

		for item in german_levels:
			label = None
			if item in input_flairs[flair].lower():
				label = item
				break

		if label != None:

			if label == 'a1' or label == 'a2' or label == 'beginner':
				names[flair] = 'beginner'
				if 'beginner' not in flairs:
					flairs['beginner'] = 1
				else:
					flairs['beginner'] = flairs['beginner'] + 1

			elif label == 'b1' or label == 'b2' or label == 'intermediate':
				names[flair] = 'intermediate'
				if 'intermediate' not in flairs:
					flairs['intermediate'] = 1
				else:
					flairs['intermediate'] = flairs['intermediate'] + 1
			elif label == 'c1' or label == 'c2' or label == 'advanced':
				names[flair] = 'advanced'
				if 'advanced' not in flairs:
					flairs['advanced'] = 1
				else:
					flairs['advanced'] = flairs['advanced'] + 1


	return flairs, names

def load_results(params=True):
	file = open('y_data/liwc_results/german_liwc.txt', 'r')
	file = file.readlines()

	results = {}
	for line in file:
		line = line.strip('\n').split('\t')
		if line[0] != 'Filename':
			i = []
			if params == True:
				for item in line[1:]:
					i.append(float(item.replace(',', '.')))
			else:
				for item in line[2:6]:
					i.append(float(item.replace(',', '.')))
			results[line[0][:len(line[0])-4]] = i
		else: 
			results[line[0]] = line[1:]
	return results

def define_inputs_half_biggest(names, results):
	c = 0
	inputs = {}
	x = {}

	for item in names:
		if item in results:
			x[item] = results[item][1]
			inputs[item] = (names[item], results[item])

	x = {key: x[key] for key in sorted(x, key=x.get)[:len(x)/2]}
	for item in x:
		del inputs[item]
	return inputs

def define_inputs(names, results):
	c = 0
	inputs = {}

	for item in names:
		
		if item in results:
			inputs[item] = (names[item], results[item])
	return inputs
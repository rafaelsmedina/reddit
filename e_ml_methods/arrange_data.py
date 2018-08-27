import networkx as nx
from sklearn.metrics import f1_score
import pickle
import random
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import KFold

datasets = ['german']

def load_flairs():
	for lang in datasets:
		g = nx.read_gpickle('../y_data/threads/nx_' + lang + '_tree')

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
	file = open('../y_data/liwc_results/german_liwc.txt', 'r')
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

def f1(expected, predicted, average):
	# macro, micro, weighted, None: shows value for each class
	# print average
	return f1_score(expected, predicted, average=average) 

def execute():
	# 01. load the flairs from the file
	flairs = load_flairs()

	# 02. arrange the names -> names[post_id] = proficiency-level || flairs[proficiency-level] = quantity 
	flairs, names = arrange_flairs(flairs)

	# 03. arrange the results -> results[post_id] = [r0, r1, r2, ..., rn]
	results = load_results(True)

	# 04. inputs[post_id] = (proficiency-level, [r0, r1, r2, ..., rn])
	inputs = define_inputs(names, results)

	# 05. count
	total = 0
	for item in flairs:
		total = total + flairs[item]
	print total
	for item in flairs:
		print item, ': ', (float(flairs[item])/total)*100, '(', flairs[item] , ')'

	level = {}

	level['beginner'] = 0 
	level['intermediate'] = 1 
	level['advanced'] = 2 
	level['native'] = 3

	x = []
	y = []

	for item in inputs:
		x.append(inputs[item][1])
		y.append(level[inputs[item][0]])

	with open('../y_data/dataset/inputs', 'wb') as f:
   		pickle.dump(inputs, f)

	with open('../y_data/dataset/x', 'wb') as f:
   		pickle.dump(x, f)

	with open('../y_data/dataset/y', 'wb') as f:
		pickle.dump(y, f)

def load():
	with open('../y_data/dataset/x', 'rb') as f:
		x = pickle.load(f)
	with open('../y_data/dataset/y', 'rb') as f:
		y = pickle.load(f)
	with open('../y_data/dataset/inputs', 'rb') as f:
		inputs = pickle.load(f)

	return x, y, inputs

def feature_selection(x, y, k=50):
	return SelectKBest(chi2, k).fit_transform(x, y)

def split(x, y):
	kf = KFold(n_splits=10, shuffle=True, random_state=2)
	return kf.split(x, y)
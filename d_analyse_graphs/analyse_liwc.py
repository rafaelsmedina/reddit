# this file gets each post with a flair and saves them for
# later run on liwc

import statistics
import networkx as nx

filename = 'liwc/results/flair/german.txt'
filenames = ['german', 'french', 'spanish', 'english']

def read_file(file):
	file = open(file)
	lines = file.readlines()
	results = {}
	for line in lines:
		line = line.strip('\n').split('\t')
		if line[0] != 'Filename':
			results[line[0][:len(line[0])-4]] = line[1:]
		else: 
			results[line[0]] = line[1:]
	return results

def analyse_flair_german(g):

	german_levels = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'beginner', 'intermediate', 'advanced', 'native']
	flairs = {}
	flairs_name = {}
	for node in g.nodes():
		if 'author_flair' in g.node[node] and g.node[node]['author_flair'] != None:
			for item in german_levels:
				label = None
				if item in g.node[node]['author_flair'].lower():
					label = item
					break
			if label != None:
				if label not in flairs:
					flairs[label] = 1
				else: 
					flairs[label] = flairs[label] + 1

				if label == 'a1' or label == 'a2' or label == 'beginner':
					flairs_name[node] = 'beginner'
				elif label == 'b1' or label == 'b2' or label == 'intermediate':
					flairs_name[node] = 'intermediate'
				elif label == 'c1' or label == 'c2' or label == 'advanced':
					flairs_name[node] = 'advanced'
				else:
					flairs_name[node] = label

	return flairs, flairs_name

def analyse_flair_german_user(g):

	german_levels = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'beginner', 'intermediate', 'advanced', 'native']
	flairs = {}
	flairs_name = {}
	for node in g.nodes():
		if 'author_flair' in g.node[node] and g.node[node]['author_flair'] != None:
			for item in german_levels:
				label = None
				if item in g.node[node]['author_flair'].lower():
					label = item
					break
			if label != None:
				if label not in flairs:
					flairs[label] = 1
				else: 
					flairs[label] = flairs[label] + 1

				if label == 'a1' or label == 'a2' or label == 'beginner':
					flairs_name[g.node[node]['author']] = 'beginner'
				elif label == 'b1' or label == 'b2' or label == 'intermediate':
					flairs_name[g.node[node]['author']] = 'intermediate'
				elif label == 'c1' or label == 'c2' or label == 'advanced':
					flairs_name[g.node[node]['author']] = 'advanced'
				else:
					flairs_name[g.node[node]['author']] = label

	return flairs, flairs_name

def calc_statistics_all(results):
	# ingles tem a estrutura diferente dos outros pq o dicionario eh mais novo
	if 'english' not in filename:
		for value in range(0, len(results['Filename'])):
			values = []
			for post in results:
				if post != 'Filename':
					if float(results[post][4].replace(',', '.')) > 40:
						values.append(float(results[post][value].replace(',', '.')))
			print results['Filename'][value], statistics.mean(values), statistics.median(values), statistics.stdev(values)

def calc_per_flair(results, flairs_name):
	# ingles tem a estrutura diferente dos outros pq o dicionario eh mais novo
	if 'english' not in filename:
		file = open('german_flair_analysis', 'a+')
		for value in range(0, len(results['Filename'])):

			values = {}

			for post in results:

				if post != 'Filename':

					if float(results[post][4].replace(',', '.')) > 40:

						if post in flairs_name:
							if flairs_name[post] not in values:
								values[flairs_name[post]] = [float(results[post][value].replace(',', '.'))]
							else:
								values[flairs_name[post]].append(float(results[post][value].replace(',', '.')))

			print>>file, results['Filename'][value]
			for item in values.keys():
				print>>file, item.capitalize()
				print>>file, 'mean: ', statistics.mean(values[item]) 
				print>>file, 'median: ', statistics.median(values[item])
				print>>file, 'stdv: ', statistics.stdev(values[item])




if __name__ == '__main__':

	g = nx.read_gpickle('german_data/nx_german_tree')

	flairs, flairs_name = analyse_flair_german_user(g)

	b = 0
	i = 0
	a = 0
	n = 0

	for item in flairs_name:
		if flairs_name[item] == 'beginner':
			b = b + 1
		elif flairs_name[item] == 'intermediate':
			i = i + 1
		elif flairs_name[item] == 'advanced':
			a = a + 1
		elif flairs_name[item] == 'native':
			n = n + 1

	print b,i,a,n

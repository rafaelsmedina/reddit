# this file gets the thread graph and analyses the 
# evolution of proficiency of users over time

import networkx as nx
import datetime
import pickle

datasets = ['german']
german_levels = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'beginner', 'intermediate', 'advanced', 'native']

hierarchy = {
	'beginner': 0,
	'intermediate': 1,
	'advanced': 2,
	'native': 3
}

for lang in datasets:
	g = nx.read_gpickle('threads/nx_' + lang + '_tree')

	users = {}

	for item in g.nodes():
		if 'author' in g.node[item] and g.node[item]['author_flair']:
			for lb in german_levels:
				label = None
				if lb in g.node[item]['author_flair'].lower():
					label = lb
					break

			if label == 'a1' or label == 'a2' or label == 'beginner':
				label = 'beginner'
			elif label == 'b1' or label == 'b2' or label == 'intermediate':
				label = 'intermediate'
			elif label == 'c1' or label == 'c2' or label == 'advanced':
				label = 'advanced'
			else:
				label = label

			if label:
				if g.node[item]['author'] in users:
					users[g.node[item]['author']][g.node[item]['date']] = (label, item.strip('u').strip('\''))
				else:
					users[g.node[item]['author']] = {}
					users[g.node[item]['author']][g.node[item]['date']] = (label, item.strip('u').strip('\''))

	probs = {}

	file = open('knn_10.csv')
	for line in file.readlines():
		id, correct, prob = line.split(',')
		probs[id.strip(' ')] = [float(i) for i in prob.strip(' [').strip(']\n').split()]

	sequences = {}
	for user in users:

		profs = []

		beg = []
		inte = []
		adv = []
		probabilities = [beg, inte, adv]

		l = users[user].keys()
		before = None

		seq = True
		for item in sorted(l):

			profs.append(hierarchy[users[user][item][0]])

			if str(users[user][item][1]) in probs:

				beg.append(probs[str(users[user][item][1])][0])
				inte.append(probs[str(users[user][item][1])][1])
				adv.append(probs[str(users[user][item][1])][2])
			else:
				seq = False

			if before == None:
				before = item
			else:
				if hierarchy[users[user][item][0]] < hierarchy[users[user][before][0]]:
					seq = False

			if not seq:
				break

		if seq and len(profs) > 1 and 3 not in profs:
			sequences[user] = (profs, probabilities)

	pickle.dump(sequences, open('sequences', 'wb'))



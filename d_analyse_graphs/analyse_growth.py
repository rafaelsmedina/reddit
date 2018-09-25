import pickle
import networkx as nx

file = open('correct', 'r')
correct = pickle.load(file)

g = nx.read_gpickle('../y_data/trees/german')
td = nx.read_gpickle('../y_data/threads/nx_german_tree')

hierarchy = {
	'beginner': 0,
	'intermediate': 1,
	'advanced': 2,
	'native': 3
}

german_levels = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'beginner', 'intermediate', 'advanced', 'native']


for user in correct:
	level = {}
	l = correct[user].keys()
	for t in sorted(l):
		if correct[user][t][0] not in level:
			level[correct[user][t][0]] = {}
		for item in correct[user][t][2]:
			if correct[user][t][1] in td[item]:
				if 'author_flair' in td.node[item] and td.node[item]['author_flair']:
					aux = td.node[item]['author_flair']

					for lb in german_levels:
						label = None
						if lb in aux.lower():
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

					if label not in level[correct[user][t][0]]:
						level[correct[user][t][0]][label] = 1
					else:
						level[correct[user][t][0]][label] += 1

		for item in td[correct[user][t][1]]:
			if 'author_flair' in td.node[item] and td.node[item]['author_flair']:
				aux = td.node[item]['author_flair']

				for lb in german_levels:
					label = None
					if lb in aux.lower():
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

				if label not in level[correct[user][t][0]]:
					level[correct[user][t][0]][label] = 1
				else:
					level[correct[user][t][0]][label] += 1			


	print user, len(correct[user]), level


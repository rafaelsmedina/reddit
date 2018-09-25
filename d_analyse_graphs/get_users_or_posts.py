import operator
import networkx as nx
import pickle


item = 'german'


g = nx.read_gpickle('../y_data/trees/' + item)
print len(g.nodes())


#in degree
ind = {}
for node in g.nodes():
	ind[node] = g.in_degree(node)
top_10_in = dict(sorted(ind.iteritems(), key=operator.itemgetter(1), reverse=True)[:50])
#print top_10_in

# file = open('../y_data/basics/' + item + '/in', 'w')
# print>>file, ind
# file.close()
print item, 'in ok'

#out degree
outd = {}
for node in g.nodes():
	outd[node] = g.out_degree(node)
top_10_out = dict(sorted(outd.iteritems(), key=operator.itemgetter(1), reverse=True)[:50])
#print top_10_out

# file = open('../y_data/basics/' + item + '/out', 'w')
# print>>file, outd
# file.close()
print item, 'out ok'

#weight
weight = {}
for edge in g.edges():
	weight[edge] = g[edge[0]][edge[1]]['weight']
top_10_wei = dict(sorted(weight.iteritems(), key=operator.itemgetter(1), reverse=True)[:50])
#print top_10_wei

# file = open('../y_data/basics/' + item + '/weight', 'w')
# print>>file, weight
# file.close()
print item, 'weight ok'

td = nx.read_gpickle('../y_data/threads/nx_' + item + '_tree')

posts = {}
user_levels = {}

for user in top_10_in:
	if user not in posts:
		posts[user] = []
		user_levels[user] = [] 

for user in top_10_out:
	if user not in posts:
		posts[user] = []
		user_levels[user] = []

for post in td.nodes():
	if 'author' in td.node[post]:
		if td.node[post]['author'] in posts:
			posts[td.node[post]['author']].append(td.node[post])

# print posts
# file = open('../y_data/basics/' + item + '/top_posts', 'w')
# print>>file, posts
# file.close()

german_levels = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'beginner', 'intermediate', 'advanced', 'native']

hierarchy = {
	'beginner': 0,
	'intermediate': 1,
	'advanced': 2,
	'native': 3
}

for item in posts:
	for post in posts[item]:
		if post['author_flair']:
			for lb in german_levels:
				label = None
				if lb in post['author_flair'].lower():
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

			if label not in user_levels[item] and label:
				user_levels[item].append(label)

print top_10_in
print top_10_out
print user_levels

growth = {}
for item in user_levels:
	if len(user_levels[item]) > 1:
		for p in td.nodes():
			if 'author' in td.node[p]:
				if td.node[p]['author'] == item and td.node[p]['author_flair']:

					for lb in german_levels:
						label = None
						if lb in td.node[p]['author_flair'].lower():
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
						if item in growth:
							growth[item][td.node[p]['date']] = (label, p, nx.ancestors(td, p), td.node[p])
						else:
							growth[item] = {}
							growth[item][td.node[p]['date']] = (label, p, nx.ancestors(td, p), td.node[p])

pickle.dump(growth, open('growth', 'wb'))

for i in growth:
	if 'alphawolf' in i:
		print i
		l = growth[i].keys()
		for t in sorted(l):
			print growth[i][t][3]['author_flair']

correct = {}
for user in growth:
	l = growth[user].keys()
	ant = None
	wrong = False
	for t in sorted(l):
		if not ant:
			ant = hierarchy[growth[user][t][0]]
		else:
			if hierarchy[growth[user][t][0]] < ant or hierarchy[growth[user][t][0]] == 3:
				wrong = True
				break
			else:
				ant = hierarchy[growth[user][t][0]]
	if not wrong:
		correct[user] = growth[user]

pickle.dump(correct, open('correct', 'wb'))

# growth contem todos os usuarios que apresentaram crescimento ao decorrer dos posts, daqueles que tiveram muitos posts

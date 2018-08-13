# this file gets the user x user graph and 
# returns the basic metrics

import networkx as nx

datasets = ['german', 'english', 'spanish', 'french']
#datasets = ['french']
for item in datasets:
	g = nx.read_gpickle(item + '_data/' + item)

	gdir = g.to_undirected()

	#basics
	file = open(item + '_data/' + item + '_basics', 'w')
	print>>file, 'name:', item
	print>>file, 'nodes:', len(g.nodes())
	print>>file, 'edges:', len(g.edges())
	print>>file, 'number of subgraphs:', len(list(nx.connected_component_subgraphs(gdir)))
	big = max(nx.connected_component_subgraphs(gdir), key=len)
	print>>file, 'biggest subgraph nodes:', len(big.nodes())
	print>>file, 'biggest sugbgraph edges:', len(big.edges())
	file.close()
	print item, 'basics ok'

	#in degree
	file = open(item + '_data/' + item + '_in_degree', 'w')
	for node in g.nodes():
		print>>file, node, ':',  g.in_degree(node), ','
	file.close()
	print item, 'in ok'

	#out degree
	file = open(item + '_data/' + item + '_out_degree', 'w')
	for node in g.nodes():
		print>>file, node, ':',  g.out_degree(node), ','
	file.close()
	print item, 'out ok'

	#weight
	file = open(item + '_data/' + item + '_weight', 'w')
	for edge in g.edges():
		print>>file, edge, ':', g[edge[0]][edge[1]]['weight'], ','
	file.close()
	print item, 'weight ok'

	#closeness
	file = open(item + '_data/' + item + '_closeness', 'w')
	closeness = nx.closeness_centrality(g)
	print>>file, closeness
	file.close()
	print item, 'closeness ok'

	#clustering
	file = open(item + '_data/' + item + '_clustering', 'w')
	clustering = nx.clustering(gdir)
	print>>file, clustering
	file.close()
	print item, 'clustering ok'

	#eccentricity
	file = open(item + '_data/' + item + '_eccentricity', 'w')
	gdir = g.to_undirected()
	big = max(nx.connected_component_subgraphs(gdir), key=len)
	ecc = nx.eccentricity(big)
	print>>file, big
	file.close()
	print item, 'eccentricity ok'
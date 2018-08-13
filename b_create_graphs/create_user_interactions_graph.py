import pymongo
import networkx as nx


if __name__ == '__main__':
	try:
		conn = pymongo.MongoClient()
		print "Database connected successfully!"
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		exit()


	g = nx.DiGraph()

	db = conn.german
	comms = db['comments']
	posts = db['posts']
	count = 0
	i = 0

	posts_dic = {}

	for item in posts.find():
		g.add_node(item['author'])
		posts_dic[item['id']] = item['author']

	comments = {}
	
	for item in comms.find():
		g.add_node(item['author'])
		comments[item['id']] = (item['author'], item['parent_id'][3:])


	for item in comments:
		c0 = comments[item][0]
		c1 = comments[item][1]
		if c1 in posts_dic:
			p = posts_dic[c1]
			if g.has_edge(c0, p):
				g[c0][p]['weight'] = g[c0][p]['weight'] + 1
			else:
				g.add_weighted_edges_from([(c0, p, 1)])
		elif c1 in comments:
			c = comments[c1][0]
			if g.has_edge(c0, c):
				g[c0][c]['weight'] = g[c0][c]['weight'] + 1
			else:
				g.add_weighted_edges_from([(c0, c, 1)])

	g.remove_node('[deleted]')

	nx.write_gpickle(g, 'trees/german')

	print len(g.nodes()), len(g.edges())
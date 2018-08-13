import pymongo
import networkx as nx
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
subreddit = 'french'

def print_tree(g, name, level = ''):
		file = open(subreddit + '_tree', 'a+')
		print>>file, level, name
		file.close()
		for item in g[name]:
			print item, g[item]
			print_tree(g, item, level + '-')

if __name__ == '__main__':
	try:
		conn = pymongo.MongoClient()
		print "Database connected successfully!"
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		exit()


	g = nx.DiGraph()

	db = conn[subreddit]
	comms = db['comments']
	posts = db['posts']
	count = 0
	i = 0

	flairs = {}
	dates = {}

	file = open(subreddit + '_flair_changes', 'a+')

	comments = {}
	for item in comms.find():
		if item['author'] not in flairs:
			flairs[item['author']] = item['author_flair_text']
			dates[item['author']] = item['created_utc']
		else:
			if flairs[item['author']] != item['author_flair_text']:
				if flairs[item['author']] != None and item['author_flair_text'] != None:
					print>>file, item['author']
					print>>file, flairs[item['author']], '>', item['author_flair_text']
					print>>file, dates[item['author']], '>', item['created_utc']
					print>>file, "*****"
					flairs[item['author']] = item['author_flair_text']
					dates[item['author']] = item['created_utc']
		g.add_node(item['id'])

		g.node[item['id']]['date'] = item['created_utc']
		g.node[item['id']]['author'] = item['author']
		g.node[item['id']]['text'] = item['body']
		g.node[item['id']]['title'] = None
		g.node[item['id']]['score'] = item['score']
		g.node[item['id']]['author_flair'] = item['author_flair_text']
		g.node[item['id']]['post_flair'] = None

		comments[item['id']] = item['parent_id'][3:]

	g.add_node('root')

	for item in posts.find():
		if item['author'] not in flairs:
			flairs[item['author']] = item['author_flair_text']
			dates[item['author']] = item['created_utc']
		else:
			if flairs[item['author']] != item['author_flair_text']:
				if flairs[item['author']] != None and item['author_flair_text'] != None:
					print>>file, item['author']
					print>>file, flairs[item['author']], '>', item['author_flair_text']
					print>>file, dates[item['author']], '>', item['created_utc']
					print>>file, "*****"
					flairs[item['author']] = item['author_flair_text']
					dates[item['author']] = item['created_utc']
		g.add_node(item['id'])
		g.node[item['id']]['date'] = item['created_utc']
		g.node[item['id']]['author'] = item['author']
		g.node[item['id']]['text'] = item['selftext']
		g.node[item['id']]['title'] = item['title']
		g.node[item['id']]['score'] = item['score']
		g.node[item['id']]['author_flair'] = item['author_flair_text']
		g.node[item['id']]['post_flair'] = item['link_flair_text']

		g.add_edge('root', item['id'])

	for item in comments:
		g.add_edge(comments[item], item)

	nx.write_gpickle(g, 'threads/nx_' + subreddit + '_tree')


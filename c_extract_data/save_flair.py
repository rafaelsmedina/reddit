# this file saves for each post/comment:
# the flair as put up by the user 

import pymongo
import networkx as nx
import sys  
import json
import datetime

reload(sys)  
sys.setdefaultencoding('utf8')
subreddits = ['english', 'french', 'spanish', 'german']

if __name__ == '__main__':
	for subreddit in subreddits:
		g = nx.read_gpickle(subreddit + '_data/nx_' + subreddit + '_tree')

		flairs = {}

		for node in g.nodes():
			if node != 'root':
				if 'author_flair' in g.node[node]:
					if g.node[node]['author_flair'] != None:
						file = open(subreddit + '/' + node + '.txt', 'w')
						flairs[node] = g.node[node]['author_flair']
						if g.node[node]['title'] != None:
							print>>file, g.node[node]['title']
						print>>file, g.node[node]['text']
						file.close()
		file = open(subreddit + '/' + 'flairs' + '.txt', 'w')
		print>>file, flairs
		file.close()
		print subreddit + 'done'


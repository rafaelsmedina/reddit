# in this file the basic metrics of threads are calculated
# such as breadth and depth

import pymongo
import networkx as nx
import sys  
import json
import datetime

reload(sys)  
sys.setdefaultencoding('utf8')
subreddits = ['english', 'french', 'spanish', 'german']

def print_tree(g, name, level = ''):
		file = open(subreddit + '_tree', 'a+')
		print>>file, level, name
		file.close()
		for item in g[name]:
			print_tree(g, item, level + '-')

def print_full_tree(g, name, level = 1):
	file = open(subreddit + '_posts_tree', 'a+')
	print>>file, g.node[name]
	file.close()

	file = open(subreddit + '_tree_levels', 'a+')
	print>>file, level, name
	file.close()

	for item in g[name]:
		print_full_tree(g, item, level + 1)

#essa funcao conta quantas postagens no subreddit estiveram em cada nivel
#o nivel 1 eh o nivel do post, nivel 2 para frente, niveis de comentarios
def count_breadth(g, name, breadth, level = 0):
	if level not in breadth:
		breadth[level] = 1
	else:
		breadth[level] = breadth[level] + 1
	for item in g[name]:
		count_breadth(g, item, breadth, level + 1)

#essa funcao conta quantas postagens cada post teve em media pra cada nivel
def avg_breadth(g):
	breadth = {}
	depth = {}
	print len(g['root'])
	for post in g['root']:
		dep = depth_single(g, post)
		for i in range(1, dep+1):
			if i not in depth:
				depth[i] = 1
			else:
				depth[i] = depth[i] + 1
	count_breadth(g, 'root', breadth)

	if 0 in breadth:
		del breadth[0]

	ret = {}
	for item in depth:
		ret[item] = float(breadth[item])/depth[item]
	return ret

def depth_single(g, name, level = 1):
	max_level = level

	for item in g[name]:
		depth = depth_single(g, item, level + 1)
		if depth > max_level:
			max_level = depth

	return max_level

def count_posts(g, name):
	total = 1
	to_visit = list(g[name])

	while len(to_visit) > 0:
		item = to_visit[0]
		total = total + 1
		to_visit = to_visit + list(g[item])
		to_visit.pop(0)

	return total

def save_post_count(g, root):
	file = open(subreddit + '_data/' + subreddit + '_post_count', 'a+')
	for item in g[root]:
		print>>file, item, ':', count_posts(g, item), ','


def count_depth(g, root):
	for post in g[root]:
		file = open(subreddit + '_depth', 'a+')
		print>>file, post, ':', depth_single(g, post), ','
		file.close()

def posts_score_time(g, root):
	file = open(subreddit + '_data/' + subreddit + '_first_reply')
	lines = file.readlines()
	file.close()

	file = open(subreddit + '_data/' + subreddit + '_depth_score_time2', 'a')

	for post in g.nodes():
		if 'score' in g.node[post]:
			print>>file, post, count_posts(g, post), g.node[post]['score'], None

	for line in lines:
		line = line.split(':')
		post = line[0][2:].strip('\'')
		time = line[1].strip('\n').strip(' ')
		#print>>file, post, count_posts(g, post), g.node[post]['score'], time

def find_biggest_thread(g):
	biggest_thread = None
	biggest_value = 0

	for node in g['root']:
		val = depth_single(g, node)
		if val > biggest_value:
			biggest_thread = node
			biggest_value = val
	return biggest_thread

def print_liwc_files(g):

	file = open(subreddit + '_tree_levels', 'r')
	lines = file.readlines()

	for line in lines:
		line = line.split(' ')[1].strip('\n')

		if line != 'root':
			if 'author_flair' in g.node[line]:
				if g.node[line]['author_flair'] != None:
					file = open('threads/' + subreddit + '/' + line + '.txt', 'w')
					if g.node[line]['title'] != None:
						print>>file, g.node[line]['title']
					print>>file, g.node[line]['text']
					file.close()



if __name__ == '__main__':

	for subreddit in subreddits:
		g = nx.read_gpickle(subreddit + '_data/nx_' + subreddit + '_tree')
		posts_score_time(g, 'root')
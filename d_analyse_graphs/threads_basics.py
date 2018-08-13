# this file gets the thread graphs and 
# returns the metrics of users/posts

import networkx as nx
from collections import Counter

datasets = ['german', 'english', 'spanish', 'french']
#datasets = ['french']

for item in datasets:

	filename = item + '_data/nx_' + item + '_tree'
	print filename

	g = nx.read_gpickle(filename)

	posts = 0
	comms = 0

	score = {}

	question = 0
	non_question = 0

	users_score_activity = {}

	monthly_activity = {}

	for i in g.nodes():
		if 'title' in g.node[i]:
			if g.node[i]['title'] == None:
				comms = comms + 1
			else:
				title = g.node[i]['title']
				text = g.node[i]['text']
				if '?' in title or 'question' in title:
					question = question + 1
				else:
					non_question = non_question + 1

				posts = posts + 1

		if 'score' in g.node[i]:
			if g.node[i]['score'] not in score:
				score[g.node[i]['score']] = 1
			else:
				score[g.node[i]['score']] = score[g.node[i]['score']] + 1

			if g.node[i]['author'] not in users_score_activity:
				users_score_activity[g.node[i]['author']] = (g.node[i]['score'], 1)
			else:
				users_score_activity[g.node[i]['author']] = (users_score_activity[g.node[i]['author']][0] + g.node[i]['score'], users_score_activity[g.node[i]['author']][1] + 1)

		if 'date' in g.node[i]:
			if len(str(g.node[i]['date'].month)) == 1:
				month = '0' + str(g.node[i]['date'].month)
			else:
				month = str(g.node[i]['date'].month)
			month_year = str(g.node[i]['date'].year) + '-' + month

			if month_year not in monthly_activity:
				monthly_activity[month_year] = 1
			else:
				monthly_activity[month_year] = monthly_activity[month_year] + 1


	file = open(item + '_data/' + item + '_comments_posts', 'w')
	print>>file, "Comentarios: ", comms
	print>>file, "Posts: ", posts
	file.close()

	file = open(item + '_data/' + item + '_score', 'w')
	print>>file, score
	file.close()

	file = open(item + '_data/' + item + '_question', 'w')
	print>>file, "Possible questions posts: ", question
	print>>file, "Possible not question posts: ", non_question
	file.close()

	file = open(item + '_data/' + item + '_user_karma', 'w')
	print>>file, users_score_activity
	file.close()

	file = open(item + '_data/' + item + '_monthly_activity', 'w')
	print>>file, monthly_activity
	file.close()

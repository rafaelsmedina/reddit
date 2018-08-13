# this files ONLY counts the user activities (posts and/or comments)

import pymongo
import networkx as nx


if __name__ == '__main__':
	try:
		conn = pymongo.MongoClient()
		print "Database connected successfully!"
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		exit()

	db = conn.english
	comms = db['comments']
	posts = db['posts']

	posts_dic = {}
	comms_dic = {}
	all_dic = {}

	for item in posts.find():
		if item['author'] in posts_dic:
			posts_dic[item['author']] = posts_dic[item['author']] + 1
			all_dic[item['author']] = all_dic[item['author']] + 1
		else:
			if item['author'] != '[deleted]':	
				posts_dic[item['author']] = 1
				all_dic[item['author']] = 1 


	for item in comms.find():
		if item['author'] in comms_dic:
			comms_dic[item['author']] = comms_dic[item['author']] + 1
			all_dic[item['author']] = all_dic[item['author']] + 1
		else:
			if item['author'] != '[deleted]':
				comms_dic[item['author']] = 1 
				all_dic[item['author']] = 1 

	file = open('english' + '_post_activity', 'w')
	print>>file, posts_dic
	file.close()

	file = open('english' + '_comment_activity', 'w')
	print>>file, comms_dic
	file.close()
	
	file = open('english' + '_all_activity', 'w')
	print>>file, all_dic
	file.close()
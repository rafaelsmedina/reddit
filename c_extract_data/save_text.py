# this file saves the title + body of posts/comments
# in order to analyse them with liwc
# 

import pymongo
import networkx as nx
import sys  
import json
import datetime

reload(sys)  
sys.setdefaultencoding('utf8')
subreddit = 'spanish'

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

if __name__ == '__main__':
	try:
		conn = pymongo.MongoClient()
		print "Database connected successfully!"
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		exit()

	db = conn[subreddit]
	comms = db['comments']
	posts = db['posts']

	comments = {}

	
	for item in comms.find():
		file = open(subreddit + '/comments/' + item['id'] + '.txt', 'a')
		print>>file, json.dumps(item['body'], default = myconverter)
		file.close()

	for item in posts.find():
		file = open(subreddit + '/posts/' + item['id']  + '.txt', 'a')
		print>>file, json.dumps(item['title'] + item['selftext'], default = myconverter)
		file.close()

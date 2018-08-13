import json 
import bz2
import sys
import pymongo
import os
from optparse import OptionParser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')

def parseDir(inputDir, ids, db):
	
	for path, subdirs, files in os.walk(inputDir):

		for archive in files:

			filepath = os.path.join(path, archive)
			if archive.endswith(".bz2") or 'RS_2017-12' in archive:
				print archive
				parseFile(filepath, ids, db)


def parseFile(inputFile, ids, db):
	if inputFile.endswith('.bz2'):
		try:
			bz_file = bz2.BZ2File(inputFile,'r')
			for line in bz_file:
				if "\"subreddit\":\"German\"" in line:
					post = json.loads(line)
					if post["id"] not in ids:
						try:
							post["created_utc"] = datetime.fromtimestamp(float(post["created_utc"]))
							db.posts.insert(post)
						except:
							db.posts.insert(post)
			print "Success!"
			
		except:
			print "Error! The file doesn`t exists or the type of the file is not bz2."
	else:
		inputFile = open(inputFile, 'r')
		for line in inputFile:
			if "\"subreddit\":\"German\"" in line:
				post = json.loads(line)
				if post["id"] not in ids:
					try:
						post["created_utc"] = datetime.fromtimestamp(float(post["created_utc"]))
						db.posts.insert(post)
					except:
						db.posts.insert(post)
		print "Success!"


if __name__ == '__main__':

	try:
		conn = pymongo.MongoClient()
		print "Database connected successfully!"
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		exit()

	db = conn.german

	# The program gives options to the user.   
	parser = OptionParser()
	parser.add_option("-d", "--directory", dest="dir",
					  help="Directory containing all files", metavar="FOLDER")
	parser.add_option("-f", "--file", dest="file",
					  help="A single file", metavar="FILE")

	(options, args) = parser.parse_args()

	inputFile = options.file
	inputDir = options.dir

	posts = db.posts.find()
	ids = {}
	for post in posts:
		ids[post["id"]] = 1

	if inputDir == None:
		parseFile(inputFile, ids, db)
	else:
		parseDir(inputDir, ids, db)





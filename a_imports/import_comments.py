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
			if archive.endswith(".bz2") or 'RC_2017-12' in archive:
				print archive
				#parseFile(filepath, ids, db)   

def parseDir_file(inputDir, inputFile, ids, db):

	for path, subdirs, files in os.walk(inputDir):

		for archive in files:

			filepath = os.path.join(path, archive)

			if(archive == inputFile):
				print archive
				parseFile(filepath, ids, db)        


def parseFile(inputFile, ids, db):

	if inputFile.endswith('.bz2'):
		try:
			bz_file = bz2.BZ2File(inputFile,'r')
			for line in bz_file:
				if "\"subreddit\":\"German\"" in line:
					comment = json.loads(line)
					if comment["id"] not in ids:
						try:
							comment["created_utc"] = datetime.fromtimestamp(float(comment["created_utc"]))
							db.comments.insert(comment)
						except:
							db.comments.insert(comment)
			print "Success!"
		
		except:
			print "Error! The file doesn`t exists or the type of the file is not bz2."

	else: 
		for line in inputFile:
			if "\"subreddit\":\"German\"" in line:
				comment = json.loads(line)
				if comment["id"] not in ids:
					try:
						comment["created_utc"] = datetime.fromtimestamp(float(comment["created_utc"]))
						db.comments.insert(comment)
					except:
						db.comments.insert(comment)
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

	comments = db.comments.find()
	ids = {}
	for comment in comments:
		ids[comment["id"]] = 1

	if inputDir == None:
		parseFile(inputFile, ids, db)
	elif inputFile == None:
		parseDir(inputDir, ids, db)
	else:
		parseDir_file(inputDir, inputFile, ids, db)






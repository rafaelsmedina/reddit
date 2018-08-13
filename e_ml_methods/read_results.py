corrects = {}
probs = {}

file = open('knn_10.csv')
for line in file.readlines():
	id, correct, prob = line.split(',')
	corrects[id] = correct
	probs[id] = [float(i) for i in prob.strip(' [').strip(']\n').split()]
	for item in probs[id]:

		print type(item)
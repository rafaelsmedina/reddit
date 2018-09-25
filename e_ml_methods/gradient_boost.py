import arrange_data
from sklearn.ensemble import GradientBoostingClassifier
import random

# arrange_data.execute()
x, y, inputs = arrange_data.load()

level = {}

level['beginner'] = 0 
level['intermediate'] = 1 
level['advanced'] = 2 
level['native'] = 3

avg = []
# x = arrange_data.feature_selection(x, y, k=70)
for train, test in arrange_data.split(x, y):

	x_train = [x[i] for i in train]
	y_train = [y[i] for i in train]


	# 07. Begin training
	gb = GradientBoostingClassifier(max_depth=5)

	gb.fit(x_train, y_train)

	# 08. Test
	r = 0
	w = 0

	#confusion = [[0 for x in range(4)] for y in range(4)] 

	#expected = []
	#predicted = []

	#for item in test:
		#k = gb.predict([x[item]])[0]
		# confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
		#expected.append([y[item]])
		#predicted.append(k)
		#if [y[item]] == k:
		#	r = r + 1
		#else:
		#	w = w + 1

	#print '----------Gradient Boost-----------'
	#print 'right: ', r
	#print 'wrong: ', w
	#print arrange_data.f1(expected, predicted, 'macro')
	#print arrange_data.f1(expected, predicted, 'micro')
	#print arrange_data.f1(expected, predicted, 'weighted')
	#avg.append(arrange_data.f1(expected, predicted, 'weighted'))
	#print arrange_data.f1(expected, predicted, None)
	# for i in range(4):
	# 	for j in range(4):
	# 		print 'ex:', i, 'pred:', j, confusion[i][j]

	file = open('grad_boost.csv', 'a')
	for item in inputs:
		print>>file, item, ',', level[inputs[item][0]], ',', gb.predict_proba([inputs[item][1]])[0]
	file.close()
	break

#a = 0
#for item in avg:
#	print item
#	a = a + item
#print a/10
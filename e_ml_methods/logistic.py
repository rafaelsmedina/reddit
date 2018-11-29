import arrange_data
from sklearn.linear_model import LogisticRegression
import random

# arrange_data.execute()
x, y, inputs = arrange_data.load()

level = {}	
level['beginner'] = 0 	
level['intermediate'] = 1 	
level['advanced'] = 2 	
level['native'] = 3
level['a1'] = 0
level['a2'] = 1
level['b1'] = 2 
level['b2'] = 3
level['c1'] = 4
level['c2'] = 5

# x = arrange_data.feature_selection(x, y, k=70)
for train, test in arrange_data.split(x, y):

	x_train = [x[i] for i in train]
	y_train = [y[i] for i in train]

	# 07. Begin training
	lr = LogisticRegression(C=1)

	lr.fit(x_train, y_train)

	# 08. Test
	r = 0
	w = 0

	confusion = [[0 for m in range(6)] for n in range(6)] 

	expected = []
	predicted = []

	for item in test:
		k = lr.predict([x[item]])[0]
		confusion[y[item]][k] = confusion[y[item]][k] + 1
		expected.append([y[item]])
		predicted.append(k)
		if [y[item]] == k:
			r = r + 1
		else:
			w = w + 1

	# print '----------Logistic Regression-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	print arrange_data.f1(expected, predicted, 'weighted')
	print confusion
	# for i in range(4):
	# 	for j in range(4):
	# 		print 'ex:', i, 'pred:', j, confusion[i][j]

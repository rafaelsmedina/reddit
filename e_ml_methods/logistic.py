import arrange_data
from sklearn.linear_model import LogisticRegression
import random

# arrange_data.execute()
x, y, inputs = arrange_data.load()

# x = arrange_data.feature_selection(x, y, k=70)
for train, test in arrange_data.split(x, y):

	x_train = [x[i] for i in train]
	y_train = [y[i] for i in train]

	# 07. Begin training
	lr = LogisticRegression(C=0.1)

	lr.fit(x_train, y_train)

	# 08. Test
	r = 0
	w = 0

	# confusion = [[0 for x in range(4)] for y in range(4)] 

	expected = []
	predicted = []

	for item in test:
		k = lr.predict([x[item]])[0]
		# confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
		expected.append([y[item]])
		predicted.append(k)
		if [y[item]] == k:
			r = r + 1
		else:
			w = w + 1

	print '----------Logistic Regression-----------'
	print 'right: ', r
	print 'wrong: ', w
	print arrange_data.f1(expected, predicted, 'weighted')
	# for i in range(4):
	# 	for j in range(4):
	# 		print 'ex:', i, 'pred:', j, confusion[i][j]

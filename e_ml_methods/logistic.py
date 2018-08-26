import arrange_data
from sklearn.linear_model import LogisticRegression
import random

f1_type = 'macro'

y_train, x_train, test_group, level, inputs = arrange_data.load()


# 07. Begin training
lr = LogisticRegression()

lr.fit(x_train, y_train)

# 08. Test
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = lr.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------Logistic Regression-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]
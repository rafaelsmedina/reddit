import arrange_data
from sklearn.ensemble import RandomForestClassifier
import random

y_train, x_train, test_group, level, inputs = arrange_data.load()

# 07. Begin training
rfc2 = RandomForestClassifier(max_depth=2, random_state=0)
rfc3 = RandomForestClassifier(max_depth=3, random_state=0)
rfc5 = RandomForestClassifier(max_depth=5, random_state=0)

rfc2.fit(x_train, y_train)
rfc3.fit(x_train, y_train)
rfc5.fit(x_train, y_train)

# 08. Test
# max depth = 2
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = rfc2.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------max_depth = 2-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

# max depth = 3
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = rfc3.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------max_depth = 3-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

# max depth = 5
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = rfc5.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------max_depth = 5-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

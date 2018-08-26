import arrange_data
from sklearn.neighbors import KNeighborsClassifier
import random

f1_type = 'macro'

y_train, x_train, test_group, level, inputs = arrange_data.load()

# 07. Begin training
neigh3 = KNeighborsClassifier(n_neighbors=3)
neigh5 = KNeighborsClassifier(n_neighbors=5)
neigh10 = KNeighborsClassifier(n_neighbors=10)
neigh20 = KNeighborsClassifier(n_neighbors=20)
neigh50 = KNeighborsClassifier(n_neighbors=50)
neigh200 = KNeighborsClassifier(n_neighbors=200)
neigh1000 = KNeighborsClassifier(n_neighbors=1000)

neigh3.fit(x_train, y_train)
neigh5.fit(x_train, y_train)
neigh10.fit(x_train, y_train)
neigh20.fit(x_train, y_train)
neigh50.fit(x_train, y_train)
neigh200.fit(x_train, y_train)
neigh1000.fit(x_train, y_train)

# 08. Test

k = 3
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = neigh3.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 3-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

k = 5
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = neigh5.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 5-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

file = open('knn_5.csv', 'a')
for item in inputs:
	print>>file, item, ',', level[inputs[item][0]], ',', neigh5.predict_proba([inputs[item][1]])[0]
file.close()

# k = 10
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = neigh10.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 10-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

file = open('knn_10.csv', 'a')
for item in inputs:
	print>>file, item, ',', level[inputs[item][0]], ',', neigh10.predict_proba([inputs[item][1]])[0]
file.close()

# k = 20
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = neigh20.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 20-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

# k = 50
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = neigh50.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 50-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

# k = 200
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = neigh200.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 200-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]

# k = 1000
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = neigh1000.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 1000-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
# for i in range(4):
# 	for j in range(4):
# 		print 'ex:', i, 'pred:', j, confusion[i][j]


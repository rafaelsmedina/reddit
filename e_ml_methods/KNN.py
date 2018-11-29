import arrange_data
from sklearn.neighbors import KNeighborsClassifier
import random

# arrange_data.execute()
x, y, inputs = arrange_data.load()

avg = []
# x = arrange_data.feature_selection(x, y, k=70)
for train, test in arrange_data.split(x, y):

	x_train = [x[i] for i in train]
	y_train = [y[i] for i in train]


	# 07. Begin training
	# neigh3 = KNeighborsClassifier(n_neighbors=3)
	# neigh5 = KNeighborsClassifier(n_neighbors=5)
	# neigh10 = KNeighborsClassifier(n_neighbors=10)
	# neigh20 = KNeighborsClassifier(n_neighbors=20)
	neigh50 = KNeighborsClassifier(n_neighbors=50)
	# neigh200 = KNeighborsClassifier(n_neighbors=200)
	# neigh1000 = KNeighborsClassifier(n_neighbors=1000)

	# neigh3.fit(x_train, y_train)
	# neigh5.fit(x_train, y_train)
	# neigh10.fit(x_train, y_train)
	# neigh20.fit(x_train, y_train)
	neigh50.fit(x_train, y_train)
	# neigh200.fit(x_train, y_train)
	# neigh1000.fit(x_train, y_train)

	# # 08. Test

	# k = 3
	# r = 0
	# w = 0

	# # confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = neigh3.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------k = 3-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# # k = 5
	# r = 0
	# w = 0

	# #confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = neigh5.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------k = 5-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# #file = open('knn_5.csv', 'a')
	# #for item in inputs:
	# #	print>>file, item, ',', level[inputs[item][0]], ',', neigh5.predict_proba([inputs[item][1]])[0]
	# #file.close()

	# # k = 10
	# r = 0
	# w = 0

	# #confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = neigh10.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------k = 10-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# #file = open('knn_10.csv', 'a')
	# #for item in inputs:
	# #	print>>file, item, ',', level[inputs[item][0]], ',', neigh10.predict_proba([inputs[item][1]])[0]
	# #file.close()

	# # k = 20
	# r = 0
	# w = 0

	# #confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = neigh20.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------k = 20-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# k = 50
	r = 0
	w = 0

	confusion = [[0 for m in range(6)] for n in range(6)] 

	expected = []
	predicted = []

	for item in test:
		k = neigh50.predict([x[item]])[0]
		confusion[y[item]][k] = confusion[y[item]][k] + 1
		expected.append([y[item]])
		predicted.append(k)
		if [y[item]] == k:
			r = r + 1
		else:
			w = w + 1

	print '----------k = 50-----------'
	print 'right: ', r
	print 'wrong: ', w
	# print arrange_data.f1(expected, predicted, 'macro')
	# print arrange_data.f1(expected, predicted, 'micro')
	avg.append(arrange_data.f1(expected, predicted, 'weighted'))
	print confusion
	# print arrange_data.f1(expected, predicted, None)
	# for i in range(4):
	# 	for j in range(4):
	# 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# # k = 200
	# r = 0
	# w = 0

	# #confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = neigh200.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------k = 200-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# # k = 1000
	# r = 0
	# w = 0

	# #confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = neigh1000.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------k = 1000-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

a = 0
for item in avg:
	print item
	a = a + item
print a/10
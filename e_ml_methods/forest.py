import arrange_data
from sklearn.ensemble import RandomForestClassifier
import random

# arrange_data.execute()
x, y, inputs = arrange_data.load()

avg = []
# x = arrange_data.feature_selection(x, y, k=70)
for train, test in arrange_data.split(x, y):

	x_train = [x[i] for i in train]
	y_train = [y[i] for i in train]

	# 07. Begin training
	rcf_a = RandomForestClassifier(max_depth=85, random_state=0, max_features=85, n_estimators=96)
	# rcf_b = RandomForestClassifier(max_depth=9, random_state=0, max_features=None, n_estimators=96)
	# rcf_c = RandomForestClassifier(max_depth=9, random_state=0, max_features=None, n_estimators=128)
	# rcf_d = RandomForestClassifier(max_depth=9, random_state=0, max_features=None, n_estimators=256)

	rcf_a.fit(x_train, y_train)
	# rcf_b.fit(x_train, y_train)
	# rcf_c.fit(x_train, y_train)
	# rcf_d.fit(x_train, y_train)

	# 08. Test
	# max depth = 2
	r = 0
	w = 0

	confusion = [[0 for m in range(6)] for n in range(6)]  

	expected = []
	predicted = []

	for item in test:
		k = rcf_a.predict([x[item]])[0]
		confusion[y[item]][k] = confusion[y[item]][k] + 1
		expected.append([y[item]])
		predicted.append(k)
		if [y[item]] == k:
			r = r + 1
		else:
			w = w + 1

	# print '----------max_depth = 2-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	#print arrange_data.f1(expected, predicted, 'macro')
	#print arrange_data.f1(expected, predicted, 'micro')
	print arrange_data.f1(expected, predicted, 'weighted')
	print confusion
	#print arrange_data.f1(expected, predicted, None)
	# for i in range(4):
	# 	for j in range(4):
	# 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# # max depth = 3
	# r = 0
	# w = 0

	# #confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = rcf_b.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------max_depth = 3-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# # max depth = 5
	# r = 0
	# w = 0

	# #confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = rcf_c.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------max_depth = 5-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

	# # max depth = 5
	# r = 0
	# w = 0

	# #confusion = [[0 for x in range(4)] for y in range(4)] 

	# expected = []
	# predicted = []

	# for item in test:
	# 	k = rcf_d.predict([x[item]])[0]
	# 	# confusion[y[item]][k] = confusion[y[item]][k] + 1
	# 	expected.append([y[item]])
	# 	predicted.append(k)
	# 	if [y[item]] == k:
	# 		r = r + 1
	# 	else:
	# 		w = w + 1

	# print '----------max_depth = 5-----------'
	# print 'right: ', r
	# print 'wrong: ', w
	# #print arrange_data.f1(expected, predicted, 'macro')
	# #print arrange_data.f1(expected, predicted, 'micro')
	# print arrange_data.f1(expected, predicted, 'weighted')
	# #print arrange_data.f1(expected, predicted, None)
	# # for i in range(4):
	# # 	for j in range(4):
	# # 		print 'ex:', i, 'pred:', j, confusion[i][j]

import arrange_data
from sklearn.neighbors import KNeighborsClassifier
import random

# 01. load the flairs from the file
flairs = arrange_data.load_flairs()

# 02. arrange the names -> names[post_id] = proficiency-level || flairs[proficiency-level] = quantity 
flairs, names = arrange_data.arrange_flairs(flairs)

# 03. arrange the results -> results[post_id] = [r0, r1, r2, ..., rn]
results = arrange_data.load_results(True)

# 04. inputs[post_id] = (proficiency-level, [r0, r1, r2, ..., rn])
inputs = arrange_data.define_inputs(names, results)

# 05. count
total = 0
for item in flairs:
	total = total + flairs[item]
print total
for item in flairs:
	print item, ': ', (float(flairs[item])/total)*100, '(', flairs[item] , ')'

# 06. split training and testing sets
small = min(flairs, key=lambda k: flairs[k])
size = flairs[small]/10

bgs = [k for k,v in inputs.items() if v[0] == 'beginner']
ints = [k for k,v in inputs.items() if v[0] == 'intermediate']
advs = [k for k,v in inputs.items() if v[0] == 'advanced']
#nats = [k for k,v in inputs.items() if v[0] == 'native']

random.shuffle(bgs)
random.shuffle(ints)
random.shuffle(advs)
#random.shuffle(nats)

test = []
test = test + random.sample(bgs, size)
test = test + random.sample(ints, size)
test = test + random.sample(advs, size)
#test = test + random.sample(nats, size)
level = {}

level['beginner'] = 0 
level['intermediate'] = 1 
level['advanced'] = 2 
#level['native'] = 3

x_train = []
y_train = []

test_group = []

for item in inputs:

	if item in test:
		test_group.append(inputs[item])
	else:
		y_train.append(level[inputs[item][0]])
		x_train.append(inputs[item][1])

# 07. Begin training
neigh5 = KNeighborsClassifier(n_neighbors=5)
neigh10 = KNeighborsClassifier(n_neighbors=10)
# neigh20 = KNeighborsClassifier(n_neighbors=20)
# neigh50 = KNeighborsClassifier(n_neighbors=50)
# neigh200 = KNeighborsClassifier(n_neighbors=200)
# neigh1000 = KNeighborsClassifier(n_neighbors=1000)

neigh5.fit(x_train, y_train)
neigh10.fit(x_train, y_train)
# neigh20.fit(x_train, y_train)
# neigh50.fit(x_train, y_train)
# neigh200.fit(x_train, y_train)
# neigh1000.fit(x_train, y_train)

# 08. Test
# k = 5
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)]

for item in test_group:
	k = neigh5.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 5-----------'
print 'right: ', r
print 'wrong: ', w
for i in range(4):
	for j in range(4):
		print 'ex:', i, 'pred:', j, confusion[i][j]

# # k = 10
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)]

for item in test_group:
	k = neigh10.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------k = 10-----------'
print 'right: ', r
print 'wrong: ', w
for i in range(4):
	for j in range(4):
		print 'ex:', i, 'pred:', j, confusion[i][j]
		
# # k = 20
# r = 0
# w = 0

# for item in test_group:
# 	if [level[item[0]]] == neigh20.predict([item[1]]):
# 		r = r + 1
# 	else:
# 		w = w + 1

# print '----------k = 20-----------'
# print 'right: ', r
# print 'wrong: ', w

# # k = 50
# r = 0
# w = 0

# for item in test_group:
# 	if [level[item[0]]] == neigh50.predict([item[1]]):
# 		r = r + 1
# 	else:
# 		w = w + 1

# print '----------k = 50-----------'
# print 'right: ', r
# print 'wrong: ', w

# # k = 200
# r = 0
# w = 0

# for item in test_group:
# 	if [level[item[0]]] == neigh200.predict([item[1]]):
# 		r = r + 1
# 	else:
# 		w = w + 1

# print '----------k = 200-----------'
# print 'right: ', r
# print 'wrong: ', w

# # k = 1000
# r = 0
# w = 0

# for item in test_group:
# 	if [level[item[0]]] == neigh1000.predict([item[1]]):
# 		r = r + 1
# 	else:
# 		w = w + 1

# print '----------k = 1000-----------'
# print 'right: ', r
# print 'wrong: ', w
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
keys = inputs.keys()

random.shuffle(keys)
test = random.sample(keys, len(keys)/10)

level = {}

level['beginner'] = 1 
level['intermediate'] = 0 
level['advanced'] = 0 
level['native'] = 0

testing = 'beginner'

print testing

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
neigh20 = KNeighborsClassifier(n_neighbors=20)
neigh50 = KNeighborsClassifier(n_neighbors=50)
neigh200 = KNeighborsClassifier(n_neighbors=200)
neigh1000 = KNeighborsClassifier(n_neighbors=1000)

neigh5.fit(x_train, y_train)
neigh10.fit(x_train, y_train)
neigh20.fit(x_train, y_train)
neigh50.fit(x_train, y_train)
neigh200.fit(x_train, y_train)
neigh1000.fit(x_train, y_train)

# 08. Test
# k = 5
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh5.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 5-----------'
print 'right: ', r
print 'wrong: ', w

# k = 10
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh10.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 10-----------'
print 'right: ', r
print 'wrong: ', w

# k = 20
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh20.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 20-----------'
print 'right: ', r
print 'wrong: ', w

# k = 50
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh50.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 50-----------'
print 'right: ', r
print 'wrong: ', w

# k = 200
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh200.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 200-----------'
print 'right: ', r
print 'wrong: ', w

# k = 1000
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh1000.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 1000-----------'
print 'right: ', r
print 'wrong: ', w

# 06. split training and testing sets
keys = inputs.keys()

random.shuffle(keys)
test = random.sample(keys, len(keys)/10)

level = {}

level['beginner'] = 0 
level['intermediate'] = 1 
level['advanced'] = 0 
level['native'] = 0

testing = 'intermediate'

print testing

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
neigh20 = KNeighborsClassifier(n_neighbors=20)
neigh50 = KNeighborsClassifier(n_neighbors=50)
neigh200 = KNeighborsClassifier(n_neighbors=200)
neigh1000 = KNeighborsClassifier(n_neighbors=1000)

neigh5.fit(x_train, y_train)
neigh10.fit(x_train, y_train)
neigh20.fit(x_train, y_train)
neigh50.fit(x_train, y_train)
neigh200.fit(x_train, y_train)
neigh1000.fit(x_train, y_train)

# 08. Test
# k = 5
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh5.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 5-----------'
print 'right: ', r
print 'wrong: ', w

# k = 10
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh10.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 10-----------'
print 'right: ', r
print 'wrong: ', w

# k = 20
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh20.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 20-----------'
print 'right: ', r
print 'wrong: ', w

# k = 50
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh50.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 50-----------'
print 'right: ', r
print 'wrong: ', w

# k = 200
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh200.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 200-----------'
print 'right: ', r
print 'wrong: ', w

# k = 1000
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh1000.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 1000-----------'
print 'right: ', r
print 'wrong: ', w

# 06. split training and testing sets
keys = inputs.keys()

random.shuffle(keys)
test = random.sample(keys, len(keys)/10)

level = {}

level['beginner'] = 0 
level['intermediate'] = 0 
level['advanced'] = 1 
level['native'] = 0

testing = 'advanced'

print testing

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
neigh20 = KNeighborsClassifier(n_neighbors=20)
neigh50 = KNeighborsClassifier(n_neighbors=50)
neigh200 = KNeighborsClassifier(n_neighbors=200)
neigh1000 = KNeighborsClassifier(n_neighbors=1000)

neigh5.fit(x_train, y_train)
neigh10.fit(x_train, y_train)
neigh20.fit(x_train, y_train)
neigh50.fit(x_train, y_train)
neigh200.fit(x_train, y_train)
neigh1000.fit(x_train, y_train)

# 08. Test
# k = 5
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh5.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 5-----------'
print 'right: ', r
print 'wrong: ', w

# k = 10
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh10.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 10-----------'
print 'right: ', r
print 'wrong: ', w

# k = 20
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh20.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 20-----------'
print 'right: ', r
print 'wrong: ', w

# k = 50
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh50.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 50-----------'
print 'right: ', r
print 'wrong: ', w

# k = 200
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh200.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 200-----------'
print 'right: ', r
print 'wrong: ', w

# k = 1000
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh1000.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 1000-----------'
print 'right: ', r
print 'wrong: ', w

# 06. split training and testing sets
keys = inputs.keys()

random.shuffle(keys)
test = random.sample(keys, len(keys)/10)

level = {}

level['beginner'] = 0 
level['intermediate'] = 0 
level['advanced'] = 0 
level['native'] = 1

testing = 'native'

print testing

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
neigh20 = KNeighborsClassifier(n_neighbors=20)
neigh50 = KNeighborsClassifier(n_neighbors=50)
neigh200 = KNeighborsClassifier(n_neighbors=200)
neigh1000 = KNeighborsClassifier(n_neighbors=1000)

neigh5.fit(x_train, y_train)
neigh10.fit(x_train, y_train)
neigh20.fit(x_train, y_train)
neigh50.fit(x_train, y_train)
neigh200.fit(x_train, y_train)
neigh1000.fit(x_train, y_train)

# 08. Test
# k = 5
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh5.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 5-----------'
print 'right: ', r
print 'wrong: ', w

# k = 10
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh10.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 10-----------'
print 'right: ', r
print 'wrong: ', w

# k = 20
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh20.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 20-----------'
print 'right: ', r
print 'wrong: ', w

# k = 50
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh50.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 50-----------'
print 'right: ', r
print 'wrong: ', w

# k = 200
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh200.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 200-----------'
print 'right: ', r
print 'wrong: ', w

# k = 1000
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == neigh1000.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------k = 1000-----------'
print 'right: ', r
print 'wrong: ', w
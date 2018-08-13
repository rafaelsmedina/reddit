import arrange_data
from sklearn.linear_model import LogisticRegression
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
lr = LogisticRegression()

lr.fit(x_train, y_train)

# 08. Test
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == lr.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------Logistic Regression-----------'
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
lr = LogisticRegression()

lr.fit(x_train, y_train)

# 08. Test
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == lr.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------Logistic Regression-----------'
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
lr = LogisticRegression()

lr.fit(x_train, y_train)

# 08. Test
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == lr.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------Logistic Regression-----------'
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
lr = LogisticRegression()

lr.fit(x_train, y_train)

# 08. Test
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == lr.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------Logistic Regression-----------'
print 'right: ', r
print 'wrong: ', w
import arrange_data
from sklearn.ensemble import RandomForestClassifier
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
	print item, ': ', (float(flairs[item])/total)*100, '(', flairs[item],')'

# 06. split training and testing sets
small = min(flairs, key=lambda k: flairs[k])
size = flairs[small]/10

bgs = [k for k,v in inputs.items() if v[0] == 'beginner']
ints = [k for k,v in inputs.items() if v[0] == 'intermediate']
advs = [k for k,v in inputs.items() if v[0] == 'advanced']
nats = [k for k,v in inputs.items() if v[0] == 'native']

random.shuffle(bgs)
random.shuffle(ints)
random.shuffle(advs)
random.shuffle(nats)

test = []
test = test + random.sample(bgs, size)
test = test + random.sample(ints, size)
test = test + random.sample(advs, size)
test = test + random.sample(nats, size)

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

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc2.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 2-----------'
print 'right: ', r
print 'wrong: ', w

# max depth = 3
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc3.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 3-----------'
print 'right: ', r
print 'wrong: ', w

# max depth = 5
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc5.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 5-----------'
print 'right: ', r
print 'wrong: ', w

# 06. split training and testing sets
small = min(flairs, key=lambda k: flairs[k])
size = flairs[small]/10

bgs = [k for k,v in inputs.items() if v[0] == 'beginner']
ints = [k for k,v in inputs.items() if v[0] == 'intermediate']
advs = [k for k,v in inputs.items() if v[0] == 'advanced']
nats = [k for k,v in inputs.items() if v[0] == 'native']

random.shuffle(bgs)
random.shuffle(ints)
random.shuffle(advs)
random.shuffle(nats)

test = []
test = test + random.sample(bgs, size)
test = test + random.sample(ints, size)
test = test + random.sample(advs, size)
test = test + random.sample(nats, size)

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

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc2.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 2-----------'
print 'right: ', r
print 'wrong: ', w

# max depth = 3
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc3.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 3-----------'
print 'right: ', r
print 'wrong: ', w

# max depth = 5
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc5.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 5-----------'
print 'right: ', r
print 'wrong: ', w

# 06. split training and testing sets
small = min(flairs, key=lambda k: flairs[k])
size = flairs[small]/10

bgs = [k for k,v in inputs.items() if v[0] == 'beginner']
ints = [k for k,v in inputs.items() if v[0] == 'intermediate']
advs = [k for k,v in inputs.items() if v[0] == 'advanced']
nats = [k for k,v in inputs.items() if v[0] == 'native']

random.shuffle(bgs)
random.shuffle(ints)
random.shuffle(advs)
random.shuffle(nats)

test = []
test = test + random.sample(bgs, size)
test = test + random.sample(ints, size)
test = test + random.sample(advs, size)
test = test + random.sample(nats, size)

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

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc2.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 2-----------'
print 'right: ', r
print 'wrong: ', w

# max depth = 3
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc3.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 3-----------'
print 'right: ', r
print 'wrong: ', w

# max depth = 5
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc5.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 5-----------'
print 'right: ', r
print 'wrong: ', w

# 06. split training and testing sets
small = min(flairs, key=lambda k: flairs[k])
size = flairs[small]/10

bgs = [k for k,v in inputs.items() if v[0] == 'beginner']
ints = [k for k,v in inputs.items() if v[0] == 'intermediate']
advs = [k for k,v in inputs.items() if v[0] == 'advanced']
nats = [k for k,v in inputs.items() if v[0] == 'native']

random.shuffle(bgs)
random.shuffle(ints)
random.shuffle(advs)
random.shuffle(nats)

test = []
test = test + random.sample(bgs, size)
test = test + random.sample(ints, size)
test = test + random.sample(advs, size)
test = test + random.sample(nats, size)

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

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc2.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 2-----------'
print 'right: ', r
print 'wrong: ', w

# max depth = 3
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc3.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 3-----------'
print 'right: ', r
print 'wrong: ', w

# max depth = 5
r = 0
w = 0

for item in test_group:
	if item[0] == testing:
		if [level[item[0]]] == rfc5.predict([item[1]]):
			r = r + 1
		else:
			w = w + 1

print '----------max_depth = 5-----------'
print 'right: ', r
print 'wrong: ', w
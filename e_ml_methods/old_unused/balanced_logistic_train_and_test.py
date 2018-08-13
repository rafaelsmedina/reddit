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
small = min(flairs, key=lambda k: flairs[k])
size = flairs[small]/10
train_size = flairs[small] - size

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
level['advanced'] = 2 
level['native'] = 3

x_train = []
y_train = []

test_group = []

for item in inputs:

	if item in test:
		test_group.append(inputs[item])
	else:
		if len(y_train) < train_size:
			y_train.append(level[inputs[item][0]])
			x_train.append(inputs[item][1])

print len(y_train)

# 07. Begin training
lr = LogisticRegression()

lr.fit(x_train, y_train)

# 08. Test
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

for item in test_group:
	k = lr.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------Logistic Regression-----------'
print 'right: ', r
print 'wrong: ', w
for i in range(4):
	for j in range(4):
		print 'ex:', i, 'pred:', j, confusion[i][j]
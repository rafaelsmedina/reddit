import arrange_data
from sklearn.ensemble import GradientBoostingClassifier
import random

f1_type = 'macro'

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
		y_train.append(level[inputs[item][0]])
		x_train.append(inputs[item][1])

# 07. Begin training
gb = GradientBoostingClassifier()

gb.fit(x_train, y_train)

# 08. Test
r = 0
w = 0

confusion = [[0 for x in range(4)] for y in range(4)] 

expected = []
predicted = []

for item in test_group:
	k = gb.predict([item[1]])[0]
	confusion[level[item[0]]][k] = confusion[level[item[0]]][k] + 1
	expected.append([level[item[0]]])
	predicted.append(k)
	if [level[item[0]]] == k:
		r = r + 1
	else:
		w = w + 1

print '----------Gradient Boost-----------'
print 'right: ', r
print 'wrong: ', w
print arrange_data.f1(expected, predicted, 'macro')
print arrange_data.f1(expected, predicted, 'micro')
print arrange_data.f1(expected, predicted, 'weighted')
print arrange_data.f1(expected, predicted, None)
for i in range(4):
	for j in range(4):
		print 'ex:', i, 'pred:', j, confusion[i][j]

file = open('grad_boost.csv', 'a')
for item in inputs:
	print>>file, item, ',', level[inputs[item][0]], ',', gb.predict_proba([inputs[item][1]])[0]
file.close()
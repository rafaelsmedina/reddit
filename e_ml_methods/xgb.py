from xgboost import XGBClassifier 
import arrange_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

x, y, inputs = arrange_data.load()

avg = []

level = {}

level['beginner'] = 0 
level['intermediate'] = 1 
level['advanced'] = 2 
level['native'] = 3


for train, test in arrange_data.split(x, y):

	x_train = np.array([x[i] for i in train])
	y_train = [y[i] for i in train]

	model = XGBClassifier(max_depth=5, booster='dart')
	model.fit(x_train, y_train)

	file = open('xg_boost.csv', 'a')
	for item in inputs:
		print>>file, item, ',', level[inputs[item][0]], ',', model.predict_proba([inputs[item][1]])[0]
	file.close()
	break

# 	expected = []
# 	predicted = []


# 	for item in test:
# 		k = model.predict([x[item]])[0]

# 		expected.append([y[item]])
# 		predicted.append(k)

# 	avg.append(arrange_data.f1(expected, predicted, 'weighted'))

# for item in avg:
# 	print item
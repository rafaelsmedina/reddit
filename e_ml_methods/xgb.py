from xgboost import XGBClassifier 
import arrange_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

x, y, inputs = arrange_data.load()

avg = []
for train, test in arrange_data.split(x, y):

	x_train = np.array([x[i] for i in train])
	y_train = [y[i] for i in train]

	model = XGBClassifier()
	model.fit(x_train, y_train)

	# # make predictions for test data
	# y_pred = model.predict(X_test)
	# predictions = [round(value) for value in y_pred]
	# # evaluate predictions
	# accuracy = accuracy_score(y_test, predictions)
	# print("Accuracy: %.2f%%" % (accuracy * 100.0))

	expected = []
	predicted = []


	for item in test:
		k = model.predict([x[item]])[0]

		expected.append([y[item]])
		predicted.append(k)

	avg.append(arrange_data.f1(expected, predicted, 'weighted'))

for item in avg:
	print item
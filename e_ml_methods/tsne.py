import numpy as np
from sklearn.manifold import TSNE
import arrange_data
import matplotlib.pyplot as plt
import pickle
from matplotlib.ticker import NullFormatter


done = True

print 'load x'
x, y, inputs = arrange_data.load()

if not done:
	print 'a'
	tsne = TSNE(n_components=2, random_state=0)
	trans_data = tsne.fit_transform(x).T

	with open('../y_data/dataset/tsne', 'wb') as tf:
			pickle.dump(tsne, tf)
	with open('../y_data/dataset/t_data', 'wb') as df:
			pickle.dump(trans_data, df)

else:
	print 'load transform'
	with open('../y_data/dataset/t_data', 'r') as lf:
			trans_data = pickle.load(lf)

c = 'r', 'g', 'b', 'c'

print 'plot'
#fig = plt.figure(figsize=(15, 8))
#ax = fig.add_subplot(2, 5, 10)
plt.scatter(trans_data[0],  trans_data[1], c=np.array(y), s=0.5, cmap=plt.cm.rainbow)
plt.title("t-SNE")
plt.axis('tight')

plt.show()
import numpy as np
from sklearn.manifold import TSNE
import arrange_data
import matplotlib.pyplot as plt
import pickle

x, y, inputs = arrange_data.load()


tsne = TSNE(n_components=2, random_state=0)
trans_data = tsne.fit_transform(x).T

with open('../y_data/dataset/tsne', 'wb') as f:
		pickle.dump(tsne, f)

ax = fig.add_subplot(2, 5, 10)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("t-SNE (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')

plt.show()
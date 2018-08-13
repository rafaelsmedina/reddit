import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

datasets = ['german', 'english', 'spanish', 'french']
plot_types = ['closeness', 'clustering', 'weight', 'depth', 'first_reply', 'post_activity', 'comment_activity']

xlabel = {}
ylabel = {}
title = {}

title['closeness'] = 'Closeness Degree Histogram'
xlabel['closeness'] = 'Closeness'
ylabel['closeness'] = 'Numero de vertices'

title['clustering'] = 'Clustering Degree Histogram'
xlabel['clustering'] = 'Clustering'
ylabel['clustering'] = 'Numero de vertices'

title['weight'] = 'Edges Weight Histogram'
xlabel['weight'] = 'Peso'
ylabel['weight'] = 'Numero de arestas'

title['depth'] = 'Depth Distribution of Trees'
xlabel['depth'] = 'Profundidade'
ylabel['depth'] = 'Numero de threads'

title['first_reply'] = 'Time Until First Reply'
xlabel['first_reply'] = 'Tempo Log(Segundos)'
ylabel['first_reply'] = 'Numero de threads'

title['post_activity'] = 'Time Until First Reply'
xlabel['post_activity'] = 'Numero de usuarios'
ylabel['post_activity'] = 'Posts publicados'

title['comment_activity'] = 'Time Until First Reply'
xlabel['comment_activity'] = 'Numero de usuarios'
ylabel['comment_activity'] = 'Comentarios publicados'


for item in datasets:

	for plot in plot_types:

		filename = item + '_data/' + item + '_' + plot 
		filename_save = item + '_data/plot/' + item + '_' + plot + '_plot.eps'
		fread = open(filename, 'r')
		c = fread.readlines()
		c2 = []

		if len(c) == 1:
			c = c[0].replace('{', '').replace('}', '').split(',')

		for i in c:
			if float(i.split(':')[1].replace(' ', '').replace(',', '')) < float('Inf'):
				c2.append(float(i.split(':')[1].replace(' ', '').replace(',', '')))

		if plot == 'weight':
			if item == 'english':
				plt.hist(c2, linewidth=0.5, edgecolor='black', bins=np.linspace(0,250,20))
			elif item == 'french':
				plt.hist(c2, linewidth=0.5, edgecolor='black', bins=np.linspace(0,90,20))
			elif item == 'german':
				plt.hist(c2, linewidth=0.5, edgecolor='black', bins=np.linspace(0,70,20))
			elif item == 'spanish':
				plt.hist(c2, linewidth=0.5, edgecolor='black', bins=np.linspace(0,130,20))
		else:
			plt.hist(c2, linewidth=0.5, edgecolor='black')
		plt.yscale('log', nonposy='clip')
		#plt.title(item.title(), fontsize=20)
		plt.xlabel(xlabel[plot], fontsize=22)
		plt.ylabel(ylabel[plot], fontsize=22)
		plt.tick_params(axis = 'both', labelsize = 16)
		plt.xlim(0)
		plt.tight_layout()
		plt.savefig(filename_save, format='eps', dpi=1000)
		#plt.show()
		plt.clf()

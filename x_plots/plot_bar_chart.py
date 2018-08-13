import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import networkx as nx
from datetime import datetime
import sys 


reload(sys)  
sys.setdefaultencoding('utf8')

datasets = ['german', 'english', 'spanish', 'french']
plot_types = ['score', 'monthly_activity', 'avg_breadth']

xlabel = {}
ylabel = {}
title = {}

title['score'] = 'Users Score'
xlabel['score'] = 'Pontuacao'
ylabel['score'] = 'Numero de usuarios'

title['monthly_activity'] = 'Monthly Activity'
xlabel['monthly_activity'] = 'Mes/Ano'
ylabel['monthly_activity'] = 'Numero de Publicacoes'

title['avg_breadth'] = 'Average breadth'
xlabel['avg_breadth'] = 'Largura media'
ylabel['avg_breadth'] = 'Numero de posts'


for item in datasets:

	for plot in plot_types:

		filename = item + '_data/' + item + '_' + plot
		filename_save = item + '_data/plot/' + item + '_' + plot + '_plot.eps'
		fread = open(filename, 'r')
		c = fread.readlines()
		c2 = {}

		if len(c) == 1:
			c = c[0].replace('{', '').replace('}', '').split(',')

		for i in c:
			left, right = i.split(':')
			if plot == 'monthly_activity':
				left = datetime.strptime(left.replace('\'','').replace(' ', '') , '%Y-%m').date()
				right = int(right)
				c2[left] = int(right)
			elif plot == 'avg_breadth':
				right = float(right)
				left = float(left)
				c2[left] = float(right)
			else:	
				right = int(right)
				left = int(left)
				c2[left] = int(right)

		if plot == 'monthly_activity':
			plt.bar(list(c2.keys()), list(c2.values()), align='center', width = 20)
		else:
			plt.bar(list(c2.keys()), list(c2.values()), align='center')
		if plot != 'avg_breadth':
			plt.yscale('log', nonposy='clip')
		plt.xlabel(xlabel[plot], fontsize=22)
		plt.ylabel(ylabel[plot], fontsize=22)
		#plt.title(item.title(), fontsize=20)
		plt.tick_params(axis = 'both', labelsize = 16)
		plt.tight_layout()
		plt.savefig(filename_save, format='eps', dpi=1000)
		plt.clf()
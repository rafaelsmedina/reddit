import numpy as np
import matplotlib.pyplot as plt


# Create data
N = 500
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi*3

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

datasets = ['german', 'english', 'spanish', 'french']
#datasets = ['french']
plot_types = ['depth_score_time2']

xlabel = {}
ylabel = {}
title = {}

for item in datasets:

	for plot in plot_types:

		filename = item + '_data/' + item + '_' + plot
		filename_save = item + '_data/plot/' + item
		read = open(filename, 'r')
		lines = read.readlines()

		if len(lines) == 1:
			lines = lines[0].replace('{', '').replace('}', '').split(',')

		xscores = []
		yscores = []
		xtimes = []
		ytimes = []
		for i in lines:
			post, depth, score, time = i.split(' ')
			xscores.append(int(depth))
			yscores.append(int(score))

		# 	time = time.strip(',\n').strip('-')
		# 	if time != 'inf':
		# 		if float(time) < 1:
		# 			t = float(time) + 1
		# 		else:
		# 			t = float(time)
		# 		xtimes.append(int(depth))
		# 		ytimes.append(t)

		# plt.xscale('log', nonposy='clip')
		# plt.scatter(ytimes, xtimes, s=area,  alpha=0.5)
		# plt.ylabel('Numero de comentarios', fontsize=22)
		# plt.xlabel('Tempo', fontsize=22)
		# plt.tick_params(axis = 'both', labelsize = 16)
		# #plt.xlim(0)
		# plt.tight_layout()
		# plt.savefig(filename_save + '_time_plot.pdf', format='pdf', dpi=1000)
		# #plt.show()
		# plt.clf()

		# Plot
		print len(xscores)
		plt.scatter(yscores, xscores, s=area, alpha=0.5)
		plt.ylabel('Numero de comentarios', fontsize=22)
		plt.xlabel('Pontuacao do post', fontsize=22)
		plt.tick_params(axis = 'both', labelsize = 16)
		plt.tight_layout()
		plt.savefig(filename_save + '_score_plot.pdf', format='pdf', dpi=1000)
		# plt.show()
		plt.clf()


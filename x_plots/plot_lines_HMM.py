#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import matplotlib.lines as mlines
import numpy as np
import matplotlib.pyplot as plt

real = {}
predicted = {}

real[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
real[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
real[2] = [0, 2, 2, 2, 2]
real[3] = [0, 1, 1]

predicted[0] = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
predicted[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
predicted[2] = [0, 1, 1, 1, 1]
predicted[3] = [0, 0, 2]

for i in range(0, 4):

	t = np.arange(0, len(real[i]), 1)

	# red dashes, blue squares and green triangles
	plt.plot(t, real[i], 'ro--', t, predicted[i], 'b^--')
	plt.xlabel('Tempo', size=14)
	plt.xticks(t)
	plt.yticks(np.arange(3), ('Iniciante', 'Intermediário', 'Avançado'), rotation='vertical', size = 8)
	plt.ylabel('Proficiência', size=14)
	blue_line = mlines.Line2D([], [], color='red', marker='o', markersize=8, label='Real')
	red_line = mlines.Line2D([], [], color='blue', marker='^', markersize=8, label='Calculado')
	plt.legend(handles=[blue_line, red_line])
	plt.show()

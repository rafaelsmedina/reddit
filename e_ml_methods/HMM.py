from scipy.stats import norm
import numpy as np
import pickle
import statistics

#file = open('sequences_only_up', 'r')
file = open('sequences', 'r')
sequences = pickle.load(file)

print len(sequences)

corretos = []
c=0
t=0
values = {}
values[0] = 0
values[1] = 1 
values[2] = 2

real = {}
predito = {}

real['0'] = 0
real['1'] = 0
real['2'] = 0
real['01'] = 0
real['02'] = 0
real['12'] = 0

predito['0'] = 0
predito['1'] = 0
predito['2'] = 0
predito['01'] = 0
predito['02'] = 0
predito['12'] = 0

for item in sequences:
	proficiencias = sequences[item][0]
	N = len(proficiencias)

	log_prob = np.asarray(sequences[item][1])

	sum_to_end = np.cumsum(log_prob[:,::-1],1)[:,::-1]

	R = log_prob.copy()
	first_change = np.ones(2)*N
	R[2,:] = np.cumsum(log_prob[2,::-1])[::-1]

	

	for j in range(1,-1,-1):
	    for i in range(N-1,-1,-1):
	        rew_stay = log_prob[j,i]+R[j,i+1] if i < N-1 else log_prob[j,i]
	        R[j,i] = max(rew_stay,R[j+1,i])
	        if rew_stay < R[j+1,i]:
	            first_change[j] = min(first_change[j],i)
	        
	# print R[:,0]
	lista = []
	
	if int(first_change[1]) >= int(first_change[0]):
		for i in range(0, int(first_change[0])):
			lista.append(0)
		for i in range(int(first_change[0]), int(first_change[1])):
			lista.append(1)
		for i in range(int(first_change[1]), len(proficiencias)):
			lista.append(2)

		print proficiencias
		if 0 in proficiencias and 1 not in proficiencias and 2 not in proficiencias:
			real['0'] = real['0'] + 1
		elif 0 not in proficiencias and 1 in proficiencias and 2 not in proficiencias:
			real['1'] = real['1'] + 1
		elif 0 not in proficiencias and 1 not in proficiencias and 2 in proficiencias:
			real['2'] = real['2'] + 1
		elif 0 in proficiencias and 1 in proficiencias and 2 not in proficiencias:
			real['01'] = real['01'] + 1
		elif 0 in proficiencias and 1 not in proficiencias and 2 in proficiencias:
			real['02'] = real['02'] + 1
		elif 0 not in proficiencias and 1 in proficiencias and 2 in proficiencias:
			real['12'] = real['12'] + 1
		print lista

		if 0 in lista and 1 not in lista and 2 not in lista:
			predito['0'] = predito['0'] + 1
		elif 0 not in lista and 1 in lista and 2 not in lista:
			predito['1'] = predito['1'] + 1
		elif 0 not in lista and 1 not in lista and 2 in lista:
			predito['2'] = predito['2'] + 1
		elif 0 in lista and 1 in lista and 2 not in lista:
			predito['01'] = predito['01'] + 1
		elif 0 in lista and 1 not in lista and 2 in lista:
			predito['02'] = predito['02'] + 1
		elif 0 not in lista and 1 in lista and 2 in lista:
			predito['12'] = predito['12'] + 1

		certos = 0
		total = 0
		for i in range(0, len(lista)):
			if proficiencias[i] == lista[i]:
				certos = certos + 1
				c=c+1
			total = total + 1
			t=t+1
			values[proficiencias[i]] = values[proficiencias[i]] + 1
		corretos.append((float(certos)/float(total))*100)
		print "{0:.2f}".format((float(certos)/float(total))*100)
		print '----'

print 'media dos acertos por post:', statistics.mean(corretos)
print 'quantidade de posts corretamente etiquetados:', "{0:.2f}".format((float(c)/float(t))*100)
print t, values
print real, predito
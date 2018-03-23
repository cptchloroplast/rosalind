# http://rosalind.info/problems/cons/
from sys import argv
f = open(argv[1], 'r')
name, seq, d = '', '', {}
s = f.readline().strip()
while s:
	if s.startswith('>'):
		name = s[1:]
		s = f.readline().strip()
		while not s.startswith('>') and s:
			seq = seq + s
			s = f.readline().strip()
		d[name] = seq
		seq = ''
f.close()
A, C, G, T, results = [], [], [], [], []
for i in range(len(d[name])):
	A.append(0)
	C.append(0)
	G.append(0)
	T.append(0)
	results.append('A')
for i in d:
	index = 0
	for j in d[i]:
		if j == 'A':
			A[index] += 1
		elif j == 'C':
			C[index] += 1
		elif j == 'G':
			G[index] += 1
		elif j == 'T':
			T[index] += 1
		index += 1
temp = 0
for i in range(len(d[name])):
	if A[i] > temp:
		temp = A[i]
		results[i] = 'A'
	if C[i] > temp:
		temp = C[i]
		results[i] = 'C'
	if G[i] > temp:
		temp = G[i]
		results[i] = 'G'
	if T[i] > temp:
		temp = T[i]
		results[i] = 'T'
	temp = 0
r = open('results_' + argv[1], 'w')
for i in results:
	r.write(i)
r.write('\n')
r.write('A: ')
for i in A:
	r.write(str(i) + ' ')
r.write('\n')
r.write('C: ')
for i in C:
	r.write(str(i) + ' ')
r.write('\n')
r.write('G: ')
for i in G:
	r.write(str(i) + ' ')
r.write('\n')
r.write('T: ')
for i in T:
	r.write(str(i) + ' ')
r.close()	

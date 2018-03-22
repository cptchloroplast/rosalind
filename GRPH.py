# http://rosalind.info/problems/grph/
from sys import argv
from itertools import combinations
f = open(argv[1], 'r')
name, seq = '', ''
d = {}
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
results = []
k = 3
r = open('results_' + argv[1], 'w')
for i, j in combinations(d, 2):
	seq1 = d[i]
	seq2 = d[j]
	if seq1[-k:] == seq2[:k]:
		r.write(i + ' ' + j + '\n')
	if seq2[-k:] == seq1[:k]:
		r.write(j + ' ' + i + '\n')
r.close()

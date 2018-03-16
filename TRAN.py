# http://rosalind.info/problems/tran/
from sys import argv
f = open(argv[1], 'r')
seq1, seq2 = '', ''
s = f.readline().strip()
if s.startswith('>'):
	s = f.readline().strip()
while not s.startswith('>') and s:
	seq1 = seq1 + s
	s = f.readline().strip()
s = f.readline().strip()
if s.startswith('>'):
	s = f.readline().strip()
while not s.startswith('>') and s:
	seq2 = seq2 + s
	s = f.readline().strip()
f.close()
ti, tv = 0, 0 
for i in range(len(seq1)):
	if seq1[i] == seq2[i]:
		continue
	else:
		if seq1[i] == 'A' and seq2[i] == 'G':
			ti += 1
		elif seq1[i] == 'G' and seq2[i] == 'A':
			ti += 1
		elif seq1[i] == 'T' and seq2[i] == 'C':
			ti += 1
		elif seq1[i] == 'C' and seq2[i] == 'T':
			ti += 1
		else:
			tv += 1
r = open('results_' + argv[1], 'w')
r.write(str(float(ti)/float(tv)))
r.close()

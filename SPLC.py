# http://rosalind.info/problems/splc/
from sys import argv
from RNACodonTable import c
f = open(argv[1], 'r')
s = f.readline().strip()
seq = ''
if s.startswith('>'):
	s = f.readline().strip()
while not s.startswith('>') and s:
	seq = seq + s
	s = f.readline().strip()
sub = f.readline().strip()
while sub:
	if sub.startswith('>'):
		sub = f.readline().strip()
	k = seq.find(sub)
	while k != -1:
		seq = seq.replace(sub, '')
		k = seq.find(sub)
	sub = f.readline().strip()
f.close()
seq = seq.replace('T', 'U')
r = open('results_' + argv[1], 'w')
for i in range(0, len(seq), 3):
	p = seq[i:i+3]
	if c[p] != 'Stop':
		r.write(c[p])
	else:
		break
r.close()


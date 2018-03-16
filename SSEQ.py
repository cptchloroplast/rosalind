# http://rosalind.info/problems/sseq/
from sys import argv
f = open(argv[1], 'r')
seq, sub = '', ''
s = f.readline().strip()
if s.startswith('>'):
	s = f.readline().strip()
while not s.startswith('>') and s:
	seq = seq + s
	s = f.readline().strip()
s = f.readline().strip()
if s.startswith('>'):
	s = f.readline().strip()
while not s.startswith('>') and s:
	sub = sub + s
	s = f.readline().strip()
f.close()
r = open('results_' + argv[1], 'w')
index = 0
for i in sub:
	l = seq.find(i, index)
	index = l + 1
	r.write(str(l+1) + ' ')
r.close()

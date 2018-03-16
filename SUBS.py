# http://rosalind.info/problems/subs/
from sys import argv
f = open(argv[1], 'r')
seq = f.readline().strip()
sub = f.readline().strip()
f.close()
r = open('results_' + argv[1], 'w')
i = seq.find(sub)
while i != -1:
	r.write(str(i+1) + ' ')
	i = seq.find(sub, i+1)
r.close()

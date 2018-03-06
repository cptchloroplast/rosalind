from sys import argv
from RNACodonTable import c
f = open(argv[1], 'r')
s = f.read().strip()
f.close()
r = open('results_' + argv[1], 'w')
for i in range(0,len(s),3):
	p = s[i:i+3]
	if c[p] != 'Stop':
		r.write(c[p])
	else:
		break
r.close()

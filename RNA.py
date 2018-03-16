# http://rosalind.info/problems/rna/
from sys import argv
f = open(argv[1], 'r')
s = f.read().strip()
f.close()
s = s.replace('T', 'U')
r = open('results_' + argv[1], 'w')
r.write(s)
r.close()

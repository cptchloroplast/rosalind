# http://rosalind.info/problems/perm/
from sys import argv
from itertools import permutations
f = open(argv[1], 'r')
s = f.readline().strip()
f.close()
s = int(s)
t = list(permutations(range(1, s+1)))
r = open('results_' + argv[1], 'w')
r.write(str(len(t)) +'\n')
for i in t:
	for j in i:
		r.write(str(j) + ' ')
	r.write('\n')
r.close()

# http://rosalind.info/problems/hamm/
from sys import argv
f = open(argv[1], 'r')
s1 = f.readline().strip()
s2 = f.readline().strip()
c = 0
for i in range(len(s1)):
	if s1[i] != s2[i]:
		c += 1
r = open('results_' + argv[1], 'w')
r.write(str(c))
r.close()

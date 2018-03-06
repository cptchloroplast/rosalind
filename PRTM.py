from sys import argv
from AAMassTable import c
f = open(argv[1], 'r')
s = f.read().strip()
f.close()
r = open('results_' + argv[1], 'w')
t = 0
for i in s:
	t = t + c[i]
r.write('%.3f' % t)
r.close()

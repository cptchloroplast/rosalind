# http://rosalind.info/problems/fib/
from sys import argv
f = open(argv[1], 'r')
s = f.readline().strip()
f.close()
n, k = s.split()
n, k = int(n), int(k)
x, y = 1, 1
for i in range(n-2):
	tot = x + k * y
	y, x = x, tot
r = open('results_' + argv[1], 'w')
r.write(str(tot))
r.close()

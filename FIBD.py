# http://rosalind.info/problems/fibd/
from sys import argv

f = open(argv[1], 'r')
n, m = f.readline().strip().split()
f.close()
n, m = int(n), int(m)
z = [1,1,1]
for i in range(3,n+1):
	if i<=m:
		val = z[i-1]+z[i-2]
		z.append(val)
	else:
		val = z[i-1]+z[i-2]-z[i-m-1]
		z.append(val)
f = open('results_'+argv[1], 'w')
f.write(str(z[len(z)-1]))
f.close()

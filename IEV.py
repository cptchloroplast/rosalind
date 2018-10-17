# http://rosalind.info/problems/iev/

from sys import argv

f = open(argv[1], 'r')
a = f.readline().strip().split(' ')
f.close()
a = map(int, a)
r = 2*(a[0]*1 + a[1]*1 + a[2]*1 + a[3]*.75 + a[4]*.5 + a[5]*0)
w = open('results_' + argv[1], 'w')
w.write(str(r))
w.close()


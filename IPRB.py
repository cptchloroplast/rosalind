# http://rosalind.info/problems/iprb/
from __future__ import division
from sys import argv
f = open(argv[1], 'r')
s = f.read().strip()
f.close()
t = s.split()
ki = float(t[0])
mi = float(t[1])
ni = float(t[2])
tot = ki+mi+ni
k = ki/tot
k1 = (ki-1)/(tot-1)
k2 = mi/(tot-1)
k3 = ni/(tot-1)
kk = k*k1
km = k*k2
kn = k*k3
m = mi/tot
m1 = ki/(tot-1)
m2 = (mi-1)/(tot-1)
m3 = ni/(tot-1)
mk = m*m1
mm = m*m2
mn = m*m3
n = ni/tot
n1 = ki/(tot-1)
n2 = mi/(tot-1)
n3 = (ni-1)/(tot-1)
nk = n*n1
nm = n*n2
nn = n*n3
p = kk+km+kn+mk+mm*(3/4)+mn*(1/2)+nk+nm*(1/2)
r = open('results_' + argv[1], 'w')
r.write('%.5f' % p)
r.close()

# http://rosalind.info/problems/dna/
from sys import argv
f = open(argv[1], 'r') 
s = f.read().strip()
f.close() 
A = s.count('A')
C = s.count('C')
G = s.count('G')
T = s.count('T')
t = [A, C, G, T]
r = open('results_' + argv[1], 'w')
for i in t:
	r.write(str(i) + ' ')
r.close()

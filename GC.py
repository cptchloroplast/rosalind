# http://rosalind.info/problems/gc/
from sys import argv
f = open(argv[1], 'r')
s = f.readline().strip()
name, freq = '', 0
while s:
	n, seq = s, ''
	s = f.readline().strip()
	while not s.startswith('>') and s:
		seq = seq + s
		s = f.readline().strip()
	GC = float(seq.count('C') + seq.count('G')) / len(seq)
	if GC > freq:
		freq = GC
		name = n[1:]
f.close()
r = open('results_' + argv[1], 'w')
r.write(name + '\n' + '%.6f' % (freq * 100))
r.close()

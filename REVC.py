from sys import argv
f = open(argv[1], 'r')
s = f.read().strip()
f.close()
t = s[::-1]
c = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
r = open('results_' + argv[1], 'w')
for i in t:
	r.write(c[i])
r.close()

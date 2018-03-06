from sys import argv
f = open(argv[1], 'r')
s = f.read().strip()
f.close()
r = open('results_' + argv[1], 'w')
for i in s:
	if i == 'T':
		r.write('U')
	else:
		r.write(i)
r.close()

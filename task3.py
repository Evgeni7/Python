#Part 3 Ex 3
dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
print "Sorted by keys:", sorted(dict.keys())
print "Sorted by values:", sorted(dict.values())
print "Sorted by values:", sorted(dict, key=dict.__getitem__)

for i in sorted(dict.keys()):
	
	print i + " => " + str(dict[i])
	

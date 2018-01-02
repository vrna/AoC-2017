import sys

file = open(sys.argv[1],"r")
data = file.readlines()

count = 0
count_p2 = 0

for line in data:
    values = line.split()

    # part 1: unizue words only
    if len(values) == len(set(values)):
        count += 1

    valid = True

    # part 2: anagrams not allowed
    for n1 in xrange(0, len(values)):

        for n2 in xrange(n1 + 1, len(values)):
            if( sorted(values[n1]) == sorted(values[n2])):
                valid = False
                break

        if not valid:
            break

    if valid:
        count_p2 += 1

print "part 1:"
print("valids", count)
print ""
print "part 2:"
print("valids p2", count_p2)

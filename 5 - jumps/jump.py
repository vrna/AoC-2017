import sys
file = open(sys.argv[1],"r")
data = file.readlines()

outbound = len(data)
pos = 0
steps = 0

while (pos >= 0 and pos < outbound):
    jump = int(data[pos])
    data[pos] = str(jump+1)
    pos += jump
    steps += 1

print steps

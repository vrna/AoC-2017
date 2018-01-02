import sys

file = open(sys.argv[1],"r")
data = file.readlines()

def countChecksum(data):

    totalSum = 0
    for line in data:
        values = map(int, line.split())
        totalSum += max(values) - min(values)

    print totalSum

countChecksum(data)

import sys

file = open(sys.argv[1],"r")
data = file.readlines()

def countChecksum(data):

    totalSum = 0
    for line in data:
        values = map(int, line.split())
        values.sort()
        size = len(values)
        for n1 in xrange(0,size):
            for n2 in xrange(n1, size):
                if( n1 != n2 ):
                    v1 = values[n1]
                    v2 = values[n2]
                    if( v2 % v1 == 0):
                        totalSum += v2 / v1

    print totalSum

countChecksum(data)

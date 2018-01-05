import sys
file = open(sys.argv[1],"r")
data = file.readlines()
banks = [int(i) for i in data[0].split()]
amountOfBanks = len(banks)

visited = dict()
steps = 0
visited[str(banks)] = steps

while (True):
    topValue = max(banks)
    maxIndex = banks.index(topValue)
    banks[maxIndex] = 0

    for i in xrange(0,topValue):
        banks[(maxIndex + 1 + i) % amountOfBanks] += 1

    steps += 1
    if( str(banks) in visited):
        break
    else:
        visited[str(banks)] = steps


print("total steps",steps)
print("cycle",steps - visited[str(banks)])

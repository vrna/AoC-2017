'''
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
'''

def countDistance(size):
    # y, x
    location = [0,0]

    # saved locations for part 2
    locs = dict()
    locs[str(location)] = 1

    # right,up,left,down
    #directions = ["right","up","left","down"]
    directionAdditions = [ [0,1], [-1,0],[0,-1],[1,0] ]
    adjacents = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    directionMark = 0
    step = 1
    stepCount = 0

    for n in xrange(1,size):
        addition = directionAdditions[directionMark % 4]
        location = [x + y for x, y in zip(location, addition)]

        # calculate the sum of the locations
        locationValue = 0
        for direction in adjacents:
            adjacent = [x + y for x, y in zip(location, direction)]
            if( str(adjacent) in locs):
                locationValue += locs[str(adjacent)]

        locs[str(location)] = locationValue

        # calculate next step
        stepCount += 1

        if( stepCount == step ):
            # switch directions
            directionMark += 1
            stepCount = 0

            if( directionMark % 2 == 0):
                step += 1

        if(locationValue > size):
            print(locationValue, "exceeds",size)
            break

countDistance(1)
countDistance(12)
countDistance(23)
countDistance(1024)
countDistance(312051)

'''
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
'''

'''
-2,-2 -2,-1 -2,0 -2,1 -2,2
-1,-2 -1,-1 -1,0 -1,1 -1,2
 0,-2  0,-1  0,0  0,1  0,2
 1,-2  1,-1  1,0  1,1  1,2
 2,-2  2,-1  2,0  2,1  2,2
'''


def countDistance(size):
    # y, x
    location = [0,0]


    # right,up,left,down
    #directions = ["right","up","left","down"]
    directionAdditions = [ [0,1], [-1,0],[0,-1],[1,0] ]
    directionMark = 0
    step = 1
    stepCount = 0

    for n in xrange(1,size):
        addition = directionAdditions[directionMark % 4]
        location = [x + y for x, y in zip(location, addition)]

        # calculate next step
        stepCount += 1

        if( stepCount == step ):
            # switch directions
            directionMark += 1
            stepCount = 0

            if( directionMark % 2 == 0):
                step += 1

    print("distance",abs(location[0]) + abs(location[1]))


countDistance(1)
countDistance(12)
countDistance(23)
countDistance(1024)
countDistance(312051)

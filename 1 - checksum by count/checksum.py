import sys
# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
# 1111 produces 4 because each digit (all 1) matches the next.
# 1234 produces 0 because no digit matches the next.
# 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

# part 1
def sumDigits(inputstr):
    memorizedNumber = -1
    first = int(inputstr[0])
    totalSum = 0
    for c in inputstr:
        currentNr = int(c)

        if(currentNr == memorizedNumber):
            totalSum += memorizedNumber

        memorizedNumber = currentNr

    if( memorizedNumber == first):
        totalSum += first

    print(inputstr, "produces", totalSum)

# part 2
def sumHalfwayDigits(inputstr):
    totalSum = 0
    strlen = len(inputstr)
    for i in xrange(0,strlen):

        currentNr = int(inputstr[i])
        comparison = int(inputstr[ (i + strlen/2) % strlen ])
        #print(currentNr, comparison)
        if(currentNr == comparison):
            totalSum += currentNr

    print(inputstr, "produces", totalSum)


# calling the program
sumDigits("1122") # 3
sumDigits("1111") # 4
sumDigits("1234") # 0
sumDigits("91212129") # 9

sumHalfwayDigits("1212") # 6
sumHalfwayDigits("1221") # 0
sumHalfwayDigits("123425") # 4
sumHalfwayDigits("123123") # 12
sumHalfwayDigits("12131415") # 4

if(len(sys.argv) > 1):
    print(sys.argv[1])
    file = open(sys.argv[1],"r")
    data = file.read().replace("\r","").replace("\n","")
    sumDigits(data)
    sumHalfwayDigits(data)

import sys



def countGroups(data, expected = -1,expectedGarb = -1):
    openGroups = 0
    closedGroups = 0
    garbage = False
    escape = False
    score = 0
    garbageCount = 0

    for d in data:
        if not garbage:
            if d == "<":
                garbage = True
            elif d == "{":
                openGroups += 1
            elif d == "}":
                closedGroups += 1
                score += openGroups
                openGroups -= 1
        else:
            if not escape:
                if d == "!":
                    escape = True
                elif d == ">":
                    garbage = False
                else:
                    garbageCount += 1
            else:
                escape = False

    #print data
    print "total score: " + str(score) + " --> " + str(("not ok", "ok")[expected < 0 or score == expected])
    print "garbage count: " + str(garbageCount) + " --> " + str(("not ok", "ok")[expectedGarb < 0 or garbageCount == expectedGarb] + "\n")


if len(sys.argv) > 1:
    file = open(sys.argv[1],"r")
    data = file.readlines()
    for dataline in data:
        countGroups(dataline,-1,-1) # 10050
else:
    # part 1
    countGroups("{}", 1, -1)
    countGroups("{{{}}}", 6, -1)
    countGroups("{{},{}}", 5, -1)
    countGroups("{{{},{},{{}}}}", 16, -1)
    countGroups("{<{},{},{{}}>}", 1, -1)
    countGroups("{<a>,<a>,<a>,<a>}",1, -1)
    countGroups("{{<a>},{<a>},{<a>},{<a>}}",9, -1)
    countGroups("{{<!>},{<!>},{<!>},{<a>}}",3, -1)

    # part 2
    countGroups("<>", -1, 0)
    countGroups("<random characters>", -1, 17)
    countGroups("<<<<>", -1, 3)
    countGroups("<{!>}>", -1, 2)
    countGroups("<!!>", -1, 0)
    countGroups("<!!!>>", -1, 0)
    countGroups("<{o\"i!a,<{i<a>", -1, 10)

import sys
from collections import Counter
file = open(sys.argv[1],"r")
data = file.readlines()

#trees = [int(i) for i in data[0].split()]

# padx (45) -> pbga, havc, qoyq

# hmm, i wouldn't even need to build a tree to find out the answer...

class Tree(object):
    def __init__(self, dataline):
        splitData = dataline.split()
        self.name = splitData[0]
        self.weight = int(splitData[1].replace("(","").replace(")",""))
        self.totalWeight = -1
        self.children = [splitData[i].replace(",","") for i in xrange(3, len(splitData))]
        # self.parent = None # ?

    def hasChild(self, childname):
        for c in self.children:
            if c == childname:
                return True
        return False

    def printTree(self, trees, depth):
        indent = " " * depth
        print( (indent + self.name + " " + str(self.treeWeight(trees))))
        depth += 1
        for c in self.children:
            trees[c].printTree(trees, depth)


    def findUnbalanced(self, trees):
        # check weight of each child
        # if any of them differs, examine it
        # if all children are unbalanced, the unbalanced one is the root

        if len(self.children) == 0:
            return

        print (self.name + " " + str(self.treeWeight(trees)))
        weights = [trees[c].treeWeight(trees) for c in self.children]

        c = Counter(weights)
        least = c.most_common()[-1][0]
        most = c.most_common()[0][0]

        underweight = False

        if(most > least):
            underweight = True
            print "tree is underweight"
        elif( most == least):
            print "tree is balanced"
            for c in self.children:
                print trees[c].name + " " + str(trees[c].treeWeight(trees))
            return
        else:
            print "tree is overweight"

        unbalanced = trees[self.children[weights.index(least)]]
        print (unbalanced.name + " is unbalanced.")

        unbalanced.findUnbalanced(trees)

    def treeWeight(self, trees):
        if self.totalWeight > 0:
            return self.totalWeight

        root = trees[self.name]
        totalWeight = root.weight

        for c in root.children:
            totalWeight += trees[c].treeWeight(trees)

        self.totalWeight = totalWeight
        return totalWeight

trees = [Tree(d) for d in data]
parents = [t for t in trees if len(t.children) > 0]

dictOfTrees = dict()
for t in trees:
    dictOfTrees[t.name] = t

# find root
root = None

for p in parents:
    childOfAny = False
    for t in parents:
        if t.hasChild(p.name):
            childOfAny = True
            break

    if not childOfAny:
        root = p
        break

print '{0} is the root'.format(root.name)

# count the root weights
root.printTree(dictOfTrees,0)
print "\nunbalanced:"
root.findUnbalanced(dictOfTrees)
#for c in root.children:
#    print (c,dictOfTrees[c].weight,treeWeight(dictOfTrees,c))

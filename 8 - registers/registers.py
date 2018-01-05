import sys
file = open(sys.argv[1],"r")
data = file.readlines()

registers = dict()

topValue = 0

import operator

def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.div,
        '%' : operator.mod,
        '^' : operator.xor,
        '<' : operator.lt,
        '<=' : operator.le,
        '==' : operator.eq,
        '!=' : operator.ne,
        '>=' : operator.ge,
        '>' : operator.gt,
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

for dataline in data:
    # c dec -10 if a >= 1
    elements = dataline.split()

    register = elements[0]
    if not register in registers:
        registers[register] = 0

    registerValue = registers[register]

    # m = (else, if)[condition]
    multiplier = (-1,1)[elements[1] == "inc"]

    c_reg = elements[4]

    if not c_reg in registers:
        registers[c_reg] = 0
    c_val = registers[c_reg]


    if eval_binary_expr(c_val,elements[5],elements[6]):
        registers[register] += multiplier * int(elements[2])
    #print (dataline + " --> " + str(registers))

    topValue = (topValue,max(registers.iteritems(), key=operator.itemgetter(1))[1]) [max(registers.iteritems(), key=operator.itemgetter(1))[1] > topValue]

print "\nfinal:"
print registers
print "max:"
print max(registers.iteritems(), key=operator.itemgetter(1))
print "top:"
print topValue

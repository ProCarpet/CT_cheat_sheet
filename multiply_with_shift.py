import numpy as np

'''
creates assembly instructions for multplication with shifting

R0 = 13 * R1 
R0 = (1 + 4 + 8) * R1 
R0 = 1 * R1 + 4 * R1 + 8 * R1

'''

reg1 = 'R0'
reg2 = 'R1'
mult = 30

multiplicators = []

while (mult > 0):
    multiplicator = 2**np.int32(np.log2(mult))
    multiplicators.append(multiplicator)
    mult -= multiplicator

multiplicators = np.array(multiplicators)
revers = multiplicators[::-1]

for i in range(0, len(revers)):
    print('LSLS', reg2+','+reg2+',#'+str(np.int32(np.log2(revers[i]))))
    print('ADDS', reg1+','+reg1+','+reg2)
    revers = revers/revers[i]
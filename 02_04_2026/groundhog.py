import sys
import stdio

numberOfTrials = int(sys.argv[1]) # get the number of trials from the command line.
numberOfIters = 0

while numberOfTrials > 0:
    numberOfTrials -= 1
    numberOfIters += 1
'''for x in range(numberOfTrials):
    pass
stdio.writeln(x)'''
stdio.writeln(numberOfIters)
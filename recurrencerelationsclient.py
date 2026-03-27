import recurrencerelations as rr
import sys
import random
import time
import stdio

numTrials = int(sys.argv[1])
MIN = 1
MAX = 2**12

elapsedRecursive = 0
elapsedIterative = 0
for x in range(numTrials):
    randomN = random.randint(MIN, MAX)
    t1 = time.time()
    rr.harmonic(randomN)
    t2 = time.time()
    elapsed = t2 - t1
    elapsedIterative += elapsed
    t3 = time.time()
    elapsed = t3 - t2
    elapsedRecursive += elapsed
    rr.recursiveHarmonic(randomN)

averageRecursive = elapsedRecursive / numTrials
averageIterative = elapsedIterative / numTrials

stdio.writeln("Average Recursive: " + str(averageRecursive))
stdio.writeln("Average Iterative: " + str(averageIterative))
if averageRecursive > averageIterative:
    stdio.writeln("Recursive")
else:
    stdio.writeln("Iterative")
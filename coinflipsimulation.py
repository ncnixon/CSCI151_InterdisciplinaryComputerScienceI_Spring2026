import stdio
import random
import sys
# numTrials = 10
# while <boolean expression>: "loop exit condition"
#   Body of the while loop

numTrials = int(sys.argv[1])

if numTrials < 0:
    pass
else:

    numberOfHeads = 0
    numberOfTails = 0
    currentTrial = 1
    while currentTrial < numTrials:
        coinFlipResult = random.randrange(0, 2)  # randrage (exclusive) [start, stop)
        isHeads = (coinFlipResult == 1)
        stdio.writeln("coinFlipResult " + str(coinFlipResult))  # concatenation
        # example = int("Hello, World") this throws a TypeError (runtime error)
        stdio.writeln(isHeads)
        if isHeads:
            numberOfHeads += 1
        else:
            numberOfTails += 1

        # currentTrial += 1
        currentTrial = currentTrial + 1

    stdio.writeln((numberOfHeads / numTrials) * 100)
    stdio.writeln((numberOfTails / numTrials) * 100)
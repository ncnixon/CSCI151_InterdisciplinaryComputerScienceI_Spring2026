import stdio
import random

coinFlipResult = random.randrange(0,2) # randrange (exclusive) [start, stop)
isHeads = (coinFlipResult == 1)
stdio.writeln("coinFlipResult " + str(coinFlipResult)) # concatenation
# example = int("Hello, World") this throws a TypeError (runtime error)
stdio.writeln(isHeads)
if isHeads:
    stdio.writeln("Tails failed!")

# if <boolean expression>
#   <statement>
#   <statement>
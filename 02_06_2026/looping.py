import sys
import stdio

THRESHOLD = 70000
OUT = 100
bitcoinPrice = float(sys.argv[1])
currentPrice = bitcoinPrice
cash = 0
numberOfIters = 0
while currentPrice < THRESHOLD and cash < OUT:
    # stdio.writeln("Buying bitcoin " + " at " + str(currentPrice))
    numberOfIters += 1
    currentPrice += 1 # currentPrice = currentPrice + 1
    cash += 1
    if cash == OUT:
        break

stdio.writeln(numberOfIters)
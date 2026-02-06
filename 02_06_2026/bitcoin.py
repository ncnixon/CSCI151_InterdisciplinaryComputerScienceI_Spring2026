import sys
import stdio
THRESHOLD = 50000
SELL = 120000
bitcoinPrice = float(sys.argv[1])

if bitcoinPrice < THRESHOLD:
    stdio.writeln("BUY")
elif bitcoinPrice == THRESHOLD:
    stdio.writeln("HOLD")
else: # greater than.
    if bitcoinPrice >= SELL:
        stdio.writeln("SELL")
    else:
        stdio.writeln("HODL")

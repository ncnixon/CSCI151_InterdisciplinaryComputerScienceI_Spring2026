import sys
import stdio
THRESHOLD = 50000
SELL = 120000
bitcoinPrice = float(sys.argv[1])
message = ""
if bitcoinPrice < THRESHOLD:
    message = "BUY"
elif bitcoinPrice == THRESHOLD:
    message = "HOLD"
else: # greater than.
    if bitcoinPrice >= SELL:
        message = "SELL"
    else:
        message = "HODL"

stdio.writeln(message)

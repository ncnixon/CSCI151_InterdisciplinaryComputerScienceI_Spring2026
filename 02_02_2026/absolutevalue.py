import sys
import stdio

argumentLength = len(sys.argv)
if not (argumentLength == 2):
    stdio.writeln("usage python mysteryprogram.py <int>")
else:
    integerValue = int(sys.argv[1])
    if integerValue < 0:
        mysteryValue = -integerValue
    else:
        mysteryValue = integerValue

    stdio.writeln(mysteryValue)
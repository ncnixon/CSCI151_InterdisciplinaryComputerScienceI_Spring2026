# import statements.
import sys
import stdio
import math

argumentLength = len(sys.argv)
if not (argumentLength == 2):
    stdio.writeln("usage python absolutevalue.py <int>")
else:
    integerValue = int(sys.argv[1])
    if integerValue < 0:
        stdio.writeln(-integerValue)
    else:
        stdio.writeln(integerValue)

    # stdio.writeln(int(math.fabs(integerValue))) above likely is a similar implementation as found in the math module*


# arbitrary global code.
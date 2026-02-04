import sys
import stdio

TWO_FIFTY_FIVE = 255
r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])

if r == g and r == b and g == 0:
    c = 0.0
    m = 0.0
    y = 0.0
    k = 1.0
else:
    w = max(r / TWO_FIFTY_FIVE, g / TWO_FIFTY_FIVE, b / TWO_FIFTY_FIVE)
    c = (w - r / TWO_FIFTY_FIVE) / w
    m = (w - g / TWO_FIFTY_FIVE) / w
    y = (w - b / TWO_FIFTY_FIVE) / w
    k = 1 - w

stdio.writeln("cyan = " + str(c))
stdio.writeln("magenta = " + str(m))
stdio.writeln("yellow = " + str(y))
stdio.writeln("black = " + str(k))
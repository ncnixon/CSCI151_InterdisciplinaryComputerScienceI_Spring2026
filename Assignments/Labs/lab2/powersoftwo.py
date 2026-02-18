import sys
import stdio
import math

n = int(sys.argv[1])
start = (2 ** (round(math.log2(n) + 1)))
while start != (2 ** 0):
    start //= 2
    stdio.writeln(start)

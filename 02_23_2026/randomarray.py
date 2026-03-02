import sys
import stdarray
import random
import stdio

n = int(sys.argv[1])
myArray = stdarray.create1D(n, 0.0)

for i in range(n):
    myArray[i] = random.randrange(1, 101)

for value in myArray:
    stdio.writeln(value)

import sys
import stdio

n = int(sys.argv[1])

fibNumbers = [0, 1]

for i in range(2, n+1):
    fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])

stdio.writeln(fibNumbers[-1])
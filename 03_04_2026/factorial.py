import sys
import stdio

def factorial(n):
    stdio.writeln("Value of n: " + str(n))
    if n == 1:
        stdio.writeln("Returning 1! = 1")
        return 1

    stdio.writeln("Returning  n: " + str(n) + " factorial(" + str(n-1) + ")")
    return n * factorial(n-1)

x = int(sys.argv[1])

factorialX = factorial(x)
stdio.writeln(factorialX)

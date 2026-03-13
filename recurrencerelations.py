# Import Statements (1)
import stdio
import sys
sys.setrecursionlimit(10**8)
RECURSIVE_MODE = "recursive"
ITERATIVE_MODE = "iterative"
DYNAMIC_MODE = "dynamic"
# Function Definitions (2)
def harmonic(n):
    harmonicSum = 0
    for i in range(1, n + 1):
        harmonicSum += 1/i

    return harmonicSum

def recursiveHarmonic(n):
    if n == 1:
        return 1

    return (1/n) + recursiveHarmonic(n-1)

def recursiveFactorial(n):
    if n == 1: return 1

    return n * recursiveFactorial(n-1)

def iterativeFactorial(n):
    factorialSum = 1
    for x in range(1, n+1):
        factorialSum *= x
    return factorialSum

def recursiveFibonacci(n):
    if n == 0: return 0
    if n == 1: return 1

    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

def iterativeFibonacci(n):
    fibonacciNumbers = [0, 1]
    for x in range(2, n+1):
        fibonacciNumbers += [fibonacciNumbers[x-1] + fibonacciNumbers[x-2]]
    return fibonacciNumbers[-1]

# Test Client

def main(argv):
    x = int(argv[0])
    mode = argv[1]
    if (mode is None
            or mode not in [RECURSIVE_MODE, ITERATIVE_MODE, DYNAMIC_MODE]):
        mode = RECURSIVE_MODE

    harmonicSums = []
    if mode == RECURSIVE_MODE:
        for n in range(1, x+1):
            harmonicSums += [recursiveHarmonic(n)]
            stdio.writeln(harmonicSums[n-1])
    elif mode == ITERATIVE_MODE:
        for n in range(1, x+1):
            harmonicSums += [harmonic(n)]
            stdio.writeln(harmonicSums[n-1])
    elif mode == DYNAMIC_MODE: # Dynamic Programming Version.
        harmonicSums += [0.0, 1.0]
        for n in range(2, x + 1):
            harmonicSums += [harmonicSums[n-1] + (1 / n)]
            stdio.writeln(harmonicSums[n])

if __name__ == '__main__':
    main(sys.argv[1:])
'''
# Arbitrary Global Code.
x = 2
harmonicX = harmonic(x)
stdio.writeln(harmonicX)
'''
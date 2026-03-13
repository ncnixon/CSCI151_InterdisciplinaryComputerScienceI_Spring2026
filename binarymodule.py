# imports
import sys
import stdio

# function definitions
def _getDigits(n):
    # how many digits will binary number have?
    i = 0
    while 2 ** i <= n:
        i += 1
    return i

def _binaryRecursiveHelper(n, numberOfDigits):
    if n == 0: return "0"

    if n == 1: return  "0" * (numberOfDigits - 1) + "1"

    currentI = numberOfDigits - 1
    if 2 ** currentI > n:
        return "0" + _binaryRecursiveHelper(n, numberOfDigits - 1)
    else:
        n -= 2 ** currentI
        return "1" + _binaryRecursiveHelper(n, numberOfDigits - 1)

def binaryRecursive(n):
    numberOfDigits = _getDigits(n)
    return _binaryRecursiveHelper(n, numberOfDigits)

def main(argv):
    n = int(argv[0])
    binaryN = binaryRecursive(n)
    stdio.writeln(binaryN)
    binaryN = binaryRecursive(6)
    stdio.writeln(binaryN)
    binaryN = binaryRecursive(2)
    stdio.writeln(binaryN)
    binaryN = binaryRecursive(1)
    stdio.writeln(binaryN)
    binaryN = binaryRecursive(0)
    stdio.writeln(binaryN)
    binaryN = binaryRecursive(17)
    stdio.writeln(binaryN)

if __name__ == '__main__':
    main(sys.argv[1:])
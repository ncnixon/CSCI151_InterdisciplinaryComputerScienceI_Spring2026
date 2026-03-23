# imports
import sys
import stdio
import math
sys.setrecursionlimit(10000)

def isPositive(n):
    return True # n[0] == "0"

# function definitions
def _getDigits(n):
    # how many digits will binary number have?
    i = 0
    while 2 ** i <= n:
        i += 1
    return i

def _binaryRecursiveHelper(n, numberOfDigits):
    # base case(s).
    if n == 0: return "0"

    if n == 1: return  "0" * (numberOfDigits - 1) + "1"

    # reduction step(s).
    currentI = numberOfDigits - 1
    if 2 ** currentI > n:
        return "0" + _binaryRecursiveHelper(n, numberOfDigits - 1)
    else:
        n -= 2 ** currentI
        return "1" + _binaryRecursiveHelper(n, numberOfDigits - 1)

def binaryRecursive(n):
    #numberOfDigits = _getDigits(n)
    numberOfDigits = n.bit_length()
    return _binaryRecursiveHelper(n, numberOfDigits)

def add(n1, n2):
    # Pad with leading zeros
    max_len = max(len(n1), len(n2))
    n1 = "0" * (max_len - len(n1)) + n1
    n2 = "0" * (max_len - len(n2)) + n2

    carry = 0
    result = ""

    # Iterate from right to left
    for i in range(max_len - 1, -1, -1):
        total = int(n1[i]) + int(n2[i]) + carry
        result += str(total % 2)
        carry = total // 2

    # Handle leftover carry
    if carry:
        result += "1"

    return result[::-1]  # reverse

def subtract(n1, n2):
    result = ""
    # observe n1 - n2 is the same as n1 + -n2 i.e., N = 2sComplement(P+1), P = 2sComplement(N-1)
    return add(n1, negative(str(n2)))
def negative(n):
    #stdio.writeln(n)
    if isPositive(n):
        # P = 2sComplement(n) + 1
        n = twosComplement(n)
        stdio.writeln(n)
        return add(n, "1")
    else:
        # N = 2sComplement(n) - 1
        n = twosComplement(n)
        return subtract(n, "1")

def twosComplement(n):
    newString = ""
    for i in range(0, len(n)):
        if n[i] == "0": newString += "1"
        elif n[i] == "1": newString += "0"
        else:
            continue # not a valid binary number*
    return newString

def main(argv):
    assert add("10", "10") == "100" # i.e., does 2 + 2 == 4?
    '''
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
    '''

if __name__ == '__main__':
    main(sys.argv[1:])
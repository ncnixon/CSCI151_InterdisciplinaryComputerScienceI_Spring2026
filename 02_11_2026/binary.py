import sys
import stdio

base10 = int(sys.argv[1]) # get a base 10 number from the command line.

# calculate the largest power of 2 that divides base10.
current = 0

while 2 ** current < base10:
    current += 1

numDigits = current + 1

# while there are powers of 2 remaining in base10, iteratively divide by 2 ** (numDigits)
binaryString = ""
while numDigits > 0:
    if 2 ** (numDigits-1) <= base10:
        binaryString += "1"
        base10 -= (2 ** (numDigits - 1))
    else:
        binaryString += "0"
    numDigits -= 1
stdio.writeln(binaryString)
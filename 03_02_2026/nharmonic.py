import sys
import stdio

def harmonic(n, x=1):
    #stdio.writeln("1")
    harmonicSum = 0
    for i in range(0, n):
        harmonicSum += 1 / ((i + 1) ** x)
    #stdio.writeln("2")
    return harmonicSum

n = int(sys.argv[1]) # get me n harmonic numbers. 1 -> n

harmonicSums2 = []
for i in range(1, n+1):
    harmonicSums2 += [harmonic(i)]

stdio.writeln(harmonicSums2[-1])
#stdio.writeln("5")

import sys
import stdio

def harmonic(n):
    #stdio.writeln("1")
    harmonicSum = 0
    for i in range(0, n):
        harmonicSum += 1 / (i + 1)
    #stdio.writeln("2")
    return harmonicSum

n = int(sys.argv[1]) # get me n harmonic numbers. 1 -> n
#stdio.writeln("3")
harmonicSums = [1.0]

for i in range(1, n):
    harmonicSums += [harmonicSums[i-1] + 1 / (i + 1)]

stdio.writeln("4")
harmonicSums2 = []
for i in range(0, n+1):
    harmonicSums2 += [harmonic(i+1)]

stdio.writeln("5")

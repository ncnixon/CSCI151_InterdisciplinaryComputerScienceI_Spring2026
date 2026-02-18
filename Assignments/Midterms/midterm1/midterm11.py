import stdio
u = [0, 1]
v = [1,0]
dotProduct = 0
for x in range(len(u)):
    dotProduct += u[x] * v[x]
stdio.writeln(dotProduct)

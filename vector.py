import stdio
import stdarray

u = [1,0]
v = [0,1]

t = stdarray.create1D(2, 0)
for x in range(len(u)):
    t[x] = u[x] + v[x]
stdio.writeln(t)

dotProduct = 0
for x in range(len(u)):
    dotProduct += u[x] * v[x]

stdio.writeln(dotProduct)

a = [1, 2, 3]
b = [3, 2, 1]
A = [a, b]
B = [b, a]
C = stdarray.create2D(2, 3, 0)
# stdio.writeln(A)
for i in range(len(A)): # iterating over the rows i.e., row major order.
    for j in range (len(A[i])):
        C[i][j] = A[i][j] + B[i][j]
stdio.writeln(C)

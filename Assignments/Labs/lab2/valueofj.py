import stdio
j = 0

for i in range(j, 10):
    j += i

stdio.writeln(j)

j = 0
for i in range(10):
    j += j

stdio.writeln(j)

for j in range(10):
    j += j

stdio.writeln(j)
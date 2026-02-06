import random
import math
import stdio
random.seed(1)

u = random.random()
v = random.random()

z = math.sin(2 * math.pi * v) * math.sqrt(-2 * math.log(u))

stdio.writeln(str(z))
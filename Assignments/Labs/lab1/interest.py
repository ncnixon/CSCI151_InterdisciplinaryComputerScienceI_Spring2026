import sys
import math
import stdio

principal = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])
amount = principal * math.e ** (r*t)
stdio.writeln(amount)
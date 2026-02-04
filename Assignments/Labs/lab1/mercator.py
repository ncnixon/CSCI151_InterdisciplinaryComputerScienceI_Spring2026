import sys
import math
import stdio

lon0 = math.radians(float(sys.argv[1]))
lat  = math.radians(float(sys.argv[2]))
lon  = math.radians(float(sys.argv[3]))

x = lon - lon0
y = 0.5 * math.log((1 + math.sin(lat)) / (1 - math.sin(lat)))

stdio.writeln(str(x) + " " + str(y))

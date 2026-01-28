import sys
import stdio

TEMPERATURE_THRESHOLD = 30.0
currentTempF = int(sys.argv[1])

#if <boolean expression>: True
    # body of the conditional.

if currentTempF < TEMPERATURE_THRESHOLD:
    stdio.writeln("Burr it's cold!")

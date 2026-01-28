import sys
import stdio

TEMPERATURE_THRESHOLD = 30.0 # assignment statement.
currentTempF = int(sys.argv[1])

#if <boolean expression>: True
    # <statement>
    # <statement>

if currentTempF < TEMPERATURE_THRESHOLD:
    stdio.writeln("Burr it's cold!")

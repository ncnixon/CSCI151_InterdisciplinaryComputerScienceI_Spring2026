import sys
import stdio

programName = sys.argv[0] # Program Name (string)
x = int(sys.argv[1]) # casting, type conversion. explicit, implicit
# int(), str(), float(), round()
# arithmetic operators %, /, +, -, *, **, //
y = 5 / 2 # implicit type conversion.
#stdio.writeln(y)
isEven = (x % 2 == 0) # comparison operator. !=, ==, >, <, >=, <=
stdio.writeln(isEven)
# what is the type of x?
#stdio.writeln(type(x))

myValue = "Hello," + "World" # Concatenation.
myOtherValue = 10 * "Hello, World"
stdio.writeln(myOtherValue)

myValue = round(2.5)
stdio.writeln(myValue)
import sys
import stdio
import stdio

#name1 = sys.argv[1]
#stdio.writeln(name1)
myList = []
collectingNames = True
while collectingNames:
    stdio.writeln("Enter a name:\n")
    name = stdio.readString()
    myList.append(name)
    # myList += [name]
    stdio.writeln("Do you want to continue?\n")
    userAnswer = stdio.readString().lower()[0]
    if userAnswer == "n":
        collectingNames = False

import stdarray
import stdio

#name1 = sys.argv[1]
#stdio.writeln(name1)
myList = []
collectingAges = True
while collectingAges:
    stdio.writeln("Enter an age:\n")
    age = stdio.readInt()
    myList.append(age)
    # myList += [name]
    stdio.writeln("Do you want to continue?\n")
    userAnswer = stdio.readString().lower()[0]
    if userAnswer == "n":
        collectingAges = False

averageAge = sum(myList) / len(myList)
stdio.writeln("Average Age: " + str(averageAge))
import stdio

myArray = []
while not stdio.isEmpty():
    integerValue = stdio.readInt()
    myArray.append(integerValue)

stdio.writeln(sum(myArray) / len(myArray))
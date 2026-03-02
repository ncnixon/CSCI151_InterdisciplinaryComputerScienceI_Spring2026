import stdio

def reverse(array):
    for x in range(len(array) // 2):
        array[x], array[len(array) - x - 1] = array[len(array) - x - 1], array[x]


a = [1, 2, 3, 4, 5, 6]
reverse(a)
stdio.writeln(a)
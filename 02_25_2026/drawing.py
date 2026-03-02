import stddraw
import stdio

stddraw.setCanvasSize(200, 200)
x = []
y = []

for i in range(1, 11):
    x.append(i)
    y.append(i)



stddraw.setXscale(0, max(x))
stddraw.setYscale(0, max(y))

for i in range(len(x)):
    stddraw.point(x[i], y[i])
    stddraw.show(1000)
    stddraw.clear()





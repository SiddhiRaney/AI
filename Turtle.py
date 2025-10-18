import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(360):
    t.color(colors[i % 6])
    t.forward(i)
    t.right(59)

turtle.done()

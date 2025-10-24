import turtle
import math

# 🐢 Turtle Setup
t = turtle.Turtle()
turtle.bgcolor("white")
t.speed(0)
t.width(2)
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# 1️⃣ Spiral Flower Pattern
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(360):
    t.color(colors[i % 6])
    t.forward(i)
    t.right(59)

# 2️⃣ Expanding Circle Pattern
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)

for i in range(50, 150, 10):
    t.color(colors[i % 6])
    t.circle(i)
    t.right(10)

# 3️⃣ Starburst
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)

for i in range(60):
    t.color(colors[i % 6])
    t.forward(200)
    t.backward(200)
    t.right(6)

# 4️⃣ Polygon Spiral
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(100):
    t.color(colors[i % 6])
    t.forward(i * 5)
    t.right(91)

# 5️⃣ Concentric Squares
t.penup()
t.goto(-50, -50)
t.pendown()

for i in range(10):
    t.color(colors[i % 6])
    for _ in range(4):
        t.forward(100 + i * 20)
        t.right(90)
    t.right(10)

# 6️⃣ Sunburst Rays
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(36):
    t.color(colors[i % 6])
    t.forward(150)
    t.backward(150)
    t.right(10)

# 7️⃣ Radiant Circles
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(6):
    t.color(colors[i])
    t.circle(100 + i * 20)

# 8️⃣ Flower Mandala
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(72):
    t.color(colors[i % 6])
    t.circle(100)
    t.right(5)

# 9️⃣ Hypnotic Rings
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(36):
    t.color(colors[i % 6])
    t.circle(50 + i * 5)
    t.right(10)

# 🔟 Zigzag Spiral
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(100):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.right(91)

# 11️⃣ Twisting Squares
t.penup()
t.goto(-50, -50)
t.pendown()

for i in range(36):
    t.color(colors[i % 6])
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

# 12️⃣ Rainbow Polygon Swirl
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(90):
    t.color(colors[i % 6])
    for _ in range(6):
        t.forward(100)
        t.right(60)
    t.right(11)

# 13️⃣ Radiant Wave Pattern
# Creates colorful waves that look like flowing ribbons.
t.penup()
t.goto(-300, 0)
t.pendown()
t.width(2)
t.speed(0)

for i in range(200):
    t.color(colors[i % 6])
    t.forward(3)
    t.left(math.sin(i / 10) * 20)
    t.forward(3)

# 14️⃣ Heart Spiral
# Draws multiple hearts in a spiral arrangement.
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)

def draw_heart(size):
    t.begin_fill()
    t.left(140)
    t.forward(size)
    t.circle(-size/2, 200)
    t.left(120)
    t.circle(-size/2, 200)
    t.forward(size)
    t.end_fill()
    t.right(140)

for i in range(30):
    t.color(colors[i % 6])
    draw_heart(50)
    t.right(12)
    t.forward(10)

# 15️⃣ Geometric Web
t.penup()
t.goto(0, 0)
t.pendown()
t.width(1)

for i in range(60):
    t.color(colors[i % 6])
    t.forward(200)
    t.right(123)
    t.forward(200)
    t.right(123)
    t.forward(200)
    t.right(123)
    t.right(6)

# 16️⃣ Spiral Triangles
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)

for i in range(60):
    t.color(colors[i % 6])
    for _ in range(3):
        t.forward(i * 5)
        t.right(120)
    t.right(10)

# 17️⃣ Daisy Flower Field
t.width(2)
positions = [(-200, 200), (200, 200), (-200, -200), (200, -200), (0, -250)]

for pos in positions:
    t.penup()
    t.goto(pos)
    t.pendown()
    for i in range(36):
        t.color(colors[i % 6])
        t.circle(40, 60)
        t.left(120)
        t.circle(40, 60)
        t.left(10)

# 18️⃣ Fractal Leaf Pattern
t.penup()
t.goto(0, -100)
t.pendown()
t.width(2)
t.color("green")

def draw_branch(length):
    if length < 10:
        return
    t.forward(length)
    t.left(30)
    draw_branch(length - 10)
    t.right(60)
    draw_branch(length - 10)
    t.left(30)
    t.backward(length)

t.left(90)
draw_branch(60)
t.right(90)

# 19️⃣ Spiral Dots Galaxy
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(150):
    t.color(colors[i % 6])
    t.dot(10)
    t.forward(i * 2)
    t.right(20)

# 20️⃣ Infinity Loop Pattern
t.penup()
t.goto(0, 0)
t.pendown()
t.width(3)

for i in range(72):
    t.color(colors[i % 6])
    t.circle(100, 90)
    t.right(90)
    t.circle(100, 90)
    t.right(5)

# 21️⃣ Final Title and Border Frame
t.penup()
t.goto(-350, -300)
t.pendown()
t.color("black")
t.width(5)

for _ in range(4):
    t.forward(700)
    t.left(90)

t.penup()
t.goto(-100, 260)
t.pendown()
t.color("darkblue")
t.write("✨ Turtle Masterpiece ✨", font=("Verdana", 20, "bold"))

# Hide the turtle cursor
t.hideturtle()
turtle.done()

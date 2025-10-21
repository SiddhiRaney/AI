import turtle

# 1️⃣ Spiral Flower Pattern
# This part draws a colorful spiral flower-like pattern.
t = turtle.Turtle()
t.speed(0)
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(360):
    t.color(colors[i % 6])
    t.forward(i)
    t.right(59)

# 2️⃣ Expanding Circle Pattern
# Draws concentric circles in different colors to create a ripple effect.
t.penup()
t.goto(0, 0)
t.pendown()
t.width(3)

for i in range(6):
    t.color(colors[i])
    t.circle(50 + i * 20)
    t.right(15)

# 3️⃣ Star Burst Pattern
# Draws a star-like pattern radiating from the center.
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)

for i in range(36):
    t.color(colors[i % 6])
    t.forward(150)
    t.backward(150)
    t.right(10)

# 4️⃣ Rotating Squares Pattern
# Creates overlapping squares rotating to form a geometric flower.
t.penup()
t.goto(-50, -50)
t.pendown()

for i in range(36):
    t.color(colors[i % 6])
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

# 5️⃣ Spiral Hexagon Pattern
# Draws a continuously rotating hexagonal spiral.
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)

for i in range(120):
    t.color(colors[i % 6])
    for _ in range(6):
        t.forward(i)
        t.right(60)
    t.right(10)

# 6️⃣ Signature and Final Touch
# Writes a signature or message at the bottom.
t.penup()
t.goto(-100, -200)
t.pendown()
t.color("black")
t.write("Art by Turtle 🐢", font=("Arial", 16, "bold"))

turtle.done()

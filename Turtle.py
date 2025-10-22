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

# 7️⃣ Colorful Polygon Spiral
# Draws polygons with an increasing number of sides, forming a spiraling rainbow pattern.
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)

for i in range(3, 10):  # from triangle to nonagon
    t.color(colors[i % 6])
    for _ in range(i):
        t.forward(50 + i * 5)
        t.right(360 / i)
    t.right(20)

# 8️⃣ Radiating Dots Pattern
# Creates a burst of small colorful dots spreading outward like confetti.
t.penup()
t.goto(0, 0)
t.pendown()

t.speed(0)
for i in range(50):
    t.color(colors[i % 6])
    t.penup()
    t.forward(i * 5)
    t.dot(10)
    t.backward(i * 5)
    t.right(15)

# 9️⃣ Hypnotic Spiral
# Draws a continuous spiral using circles that gradually shrink.
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(100):
    t.color(colors[i % 6])
    t.circle(100 - i, 90)
    t.left(20)

# 🔟 Petal Mandala
# Creates a beautiful mandala with repeated petal-shaped curves.
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)

for i in range(36):
    t.color(colors[i % 6])
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(10)

# 11️⃣ Sun Rays
# Draws bright sun-like rays from the center for a glowing look.
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(72):
    t.color("gold")
    t.forward(200)
    t.backward(200)
    t.right(5)

# 12️⃣ Final Signature Glow
# Adds a glow circle around the signature for finishing touch.
t.penup()
t.goto(-100, -210)
t.pendown()
t.color("orange")
t.width(3)
t.circle(40)

t.penup()
t.goto(-130, -220)
t.pendown()
t.color("black")
t.write("Turtle Art Complete 🌸", font=("Comic Sans MS", 14, "bold"))

turtle.done()

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
# Creates a complex web-like structure using overlapping lines.
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
# Draws triangles expanding in a spiral pattern.
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
# Draws multiple flower-like patterns at different positions.
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
# Creates recursive leaves for a fractal look.
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
# Creates a galactic spiral made of colorful dots.
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(150):
    t.color(colors[i % 6])
    t.dot(10)
    t.forward(i * 2)
    t.right(20)

# 20️⃣ Infinity Loop Pattern
# Draws looping infinity curves with rotating colors.
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
# Draws a finishing frame and a title for the entire artwork.
t.penup()
t.goto(-350, -300)
t.pendown()
t.color("black")
t.width(5)

for _ in range(4):
    t.forward(700)
    t.left(90)

t.penup()
t.goto(-80, 250)
t.pendown()
t.color("darkblue")
t.write("✨ Turtle Masterpiece ✨", font=("Verdana", 20, "bold"))

# Hide the turtle cursor
t.hideturtle()
turtle.done()

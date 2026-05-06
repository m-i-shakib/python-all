import turtle
import math
import time

# ---------- Screen setup ----------
screen = turtle.Screen()
screen.title("Love Animation ❤️")
screen.bgcolor("black")
screen.setup(width=900, height=700)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# ---------- Heart parametric curve ----------
def heart_xy(a):
    x = 16 * math.sin(a) ** 3
    y = 13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)
    return x, y

def draw_heart(scale=18, color="red"):
    t.color(color)
    t.penup()

    # start point
    x0, y0 = heart_xy(0)
    t.goto(x0 * scale, y0 * scale - 40)
    t.pendown()

    # draw curve
    step = 0.02
    a = 0.0
    while a <= math.tau + step:
        x, y = heart_xy(a)
        t.goto(x * scale, y * scale - 40)
        a += step

def write_text(msg="I LOVE YOU", size=32, color="white"):
    t.penup()
    t.goto(0, -250)
    t.color(color)
    t.write(msg, align="center", font=("Arial", size, "bold"))

# ---------- Animation loop ----------
def animate():
    base = 17
    pulse = 0.0

    while True:
        t.clear()

        # pulsing scale (like heartbeat)
        s = base + 2.8 * (1 + math.sin(pulse))  # scale changes smoothly
        pulse += 0.12

        # gradient-ish effect by drawing multiple layers
        for i in range(6, 0, -1):
            layer_scale = s - i * 0.9
            # slightly different reds
            shade = 255 - i * 18
            t.pencolor((1.0, shade/255.0 * 0.12, shade/255.0 * 0.12))
            draw_heart(scale=layer_scale)

        write_text("I LOVE YOU ❤️", size=34, color="white")

        screen.update()
        time.sleep(0.02)

# turtle needs manual screen updates for smooth animation
screen.tracer(0, 0)

try:
    animate()
except turtle.Terminator:
    pass


import turtle
import random
import time

# SET UP THE SCREEN
screen = turtle.Screen()
screen.title("NEON RACER")
screen.bgcolor("#101828")
screen.setup(width=600, height=700)
screen.tracer(0)

# ROAD
road = turtle.Turtle()
road.speed(0)
road.color("#444444")
road.penup()
road.goto(-200, -350)
road.begin_fill()

for _ in range(2):
    road.forward(400)
    road.left(90)
    road.forward(700)
    road.left(90)

road.end_fill()
road.hideturtle()

# ROAD LINES
lines = []

for y in range(-330, 350, 100):
    line = turtle.Turtle()
    line.shape("square")
    line.color("white")
    line.shapesize(stretch_wid=3, stretch_len=0.15)
    line.penup()
    line.goto(0, y)
    lines.append(line)

# PLAYER CAR
player = turtle.Turtle()
player.shape("square")
player.color("#00e5ff")
player.shapesize(stretch_wid=2, stretch_len=1)
player.penup()
player.goto(0, -250)

# ENEMY CARS
enemies = []

for _ in range(3):
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color(random.choice(["red", "orange", "purple"]))
    enemy.shapesize(stretch_wid=2, stretch_len=1)
    enemy.penup()
    enemy.goto(random.choice([-140, 0, 140]), random.randint(100, 500))
    enemies.append(enemy)

# SCORE
score = 0
speed = 5

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(-270, 310)

# GAME OVER
game_over = False

# MOVEMENT
def move_left():
    x = player.xcor()
    if x > -140:
        player.setx(x - 140)

def move_right():
    x = player.xcor()
    if x < 140:
        player.setx(x + 140)

def accelerate():
    global speed
    speed = min(speed + 1, 15)

def slow_down():
    global speed
    speed = max(speed - 1, 2)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(accelerate, "Up")
screen.onkeypress(slow_down, "Down")

# MAIN GAME LOOP
while not game_over:
    screen.update()
    time.sleep(0.02)

    # MOVE ROAD LINES
    for line in lines:
        y = line.ycor() - speed
        if y < -350:
            y = 350
        line.sety(y)

    # MOVE ENEMY CARS
    for enemy in enemies:
        enemy.sety(enemy.ycor() - speed)

        if enemy.ycor() < -350:
            enemy.goto(
                random.choice([-140, 0, 140]),
                random.randint(350, 600)
            )
            score += 1
            speed = min(speed + 0.2, 15)

        # COLLISION DETECTION
        if player.distance(enemy) < 35:
            game_over = True

    # UPDATE SCORE
    score_display.clear()
    score_display.write(
        f"SCORE: {score}   SPEED: {int(speed)}",
        font=("Arial", 16, "bold")
    )

# GAME OVER SCREEN
screen.update()

message = turtle.Turtle()
message.hideturtle()
message.color("red")
message.penup()
message.goto(0, 20)
message.write(
    "GAME OVER!",
    align="center",
    font=("Arial", 35, "bold")
)

message.goto(0, -30)
message.color("white")
message.write(
    f"FINAL SCORE: {score}",
    align="center",
    font=("Arial", 18, "bold")
)

screen.mainloop()

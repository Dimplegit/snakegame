import turtle
import time
import random

delay = 0.1  # Speed of snake
paused = False  # Flag to track if the game is paused

# Set up the screen
wn = turtle.Screen()
wn.title("Dimple's Snake Game")
wn.bgcolor("white")
wn.setup(width=500 ,height=500)
wn.tracer(0)

# Set a background image (make sure the image is a .gif file and in the same directory)
wn.bgpic("bg_img.gif")  # Replace with the name of your .gif image

# Creating snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Function to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Functions to change the snake's direction
def go_up():
    if head.direction != "down":  # Prevents going in the opposite direction
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Function to toggle pause
def toggle_pause():
    global paused
    paused = not paused  # Toggle the paused state

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
wn.onkey(toggle_pause, "space")  # Bind the space bar to toggle pause

# Main game loop
while True:
    wn.update()

    # Only update the game state if not paused
    if not paused:
        # Check for the border collision
        if head.xcor() > 600 or head.xcor() < -600 or head.ycor() > 310 or head.ycor() < -310:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)  # Move segments off-screen

            # Clear the segment list
            segments.clear()

        # Check for collision with food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Add a segment to the snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("red")
            new_segment.penup()
            segments.append(new_segment)

        # Move the segments in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        time.sleep(delay)

wn.mainloop()

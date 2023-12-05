import random
import turtle


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        self.xpos = random.randint(ball_radius, canvas_width - ball_radius)
        self.ypos = random.randint(ball_radius, canvas_height - ball_radius)
        self.vx = random.randint(1, 0.01 * canvas_width)
        self.vy = random.randint(1, 0.01 * canvas_height)
        self.size = ball_radius
        self.ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move_circle(self, canvas_width, canvas_height):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (canvas_width - self.size):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (canvas_height - self.size):
            self.vy = -self.vy

    def draw_circle(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.goto(self.xpos, self.ypos - self.size)
        turtle.pendown()
        turtle.color(self.ball_color)
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()


class BallSimulator:

    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls):
        self.ball = [Ball(canvas_width, canvas_height, ball_radius) for _ in range(num_balls)]
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def update_balls(self):
        for ball in self.ball:
            ball.move_circle(self.canvas_width, self.canvas_height)

    def draw_balls(self):
        for ball in self.ball:
            ball.draw_circle()


num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width, canvas_height = turtle.screensize()
ball_radius = 0.05 * canvas_width
turtle.colormode(255)

simulator = BallSimulator(canvas_width, canvas_height, ball_radius, num_balls)

while True:
    turtle.clear()
    simulator.update_balls()
    simulator.draw_balls()
    turtle.update()

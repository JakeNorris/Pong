from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Multiply by -1 so the ball gives the appearance of bouncing on the y-axis
    def bounce_y(self):
        self.y_move *= -1

    # Multiply by -1 so the ball gives the appearance of bouncing on the x-axis
    # Also speed up the ball to increase difficulty
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    # Bring ball back to start position then set movement speed back to the start speed
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

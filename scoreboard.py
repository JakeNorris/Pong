from turtle import Turtle

# These are constant variables, so they can be easily changed from the top of the code
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # This method will clear the old score off the screen and update with the new score
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    # Used for when left paddle scores a point
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Used for when right paddle scores a point
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


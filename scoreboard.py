from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.updateScore()

    def updateScore(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

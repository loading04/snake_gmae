from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScore()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.updateScore()

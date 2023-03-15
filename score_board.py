from turtle import Turtle
FONT = ("Courier", 10, "normal")
ALIGN = "center"



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
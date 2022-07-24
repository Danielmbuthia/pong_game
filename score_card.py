from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.clear()
        self.l_score = 0
        self.r_score = 0
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Left player score {self.l_score}  Right player score {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def l_increment_score(self):
        self.l_score += 1
        self.update_score_board()

    def r_increment_score(self):
        self.r_score += 1
        self.update_score_board()

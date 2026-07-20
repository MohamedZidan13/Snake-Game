from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.Score_count = 0
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.update_score_boeard()

    def update_score_boeard(self):
        self.write(f"Score: {self.Score_count}",align="center",font=("arial",24,"normal"))

    def increase_score(self):
        self.Score_count += 1
        self.clear()
        self.update_score_boeard()

    def game_over(self):
        self.screen.bgcolor("dark red")
        self.goto(0,0)
        self.write(f"You lose! \nFinal Score: {self.Score_count}",align="center",font=("arial",24,"normal"))
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time
window = Screen()
window.setup(width=800,height=800)
window.bgcolor("black")
window.tracer(0)

tom = Snake()
food = Food()
score = Score()

window.update()

game_on = True
while game_on:
    tom.move()
    window.update()
    time.sleep(0.09)

    window.listen()
    window.onkey(tom.up,"w")
    window.onkey(tom.down,"s")
    window.onkey(tom.right,"d")
    window.onkey(tom.left,"a")

    if tom.head.distance(food) <15 :
        food.appear()
        tom.extend()

        score.increase_score()
    if tom.head.xcor() > 370 or tom.head.xcor() < -370 or tom.head.ycor() > 370 or tom.head.ycor() < -370:
        game_on = False
        score.game_over()
    for segment in tom.turtles[0:-1]:
        if tom.head.distance(segment) < 10:
            game_on = False
            score.game_over()
window.exitonclick()

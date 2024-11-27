from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.write_score()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_up()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
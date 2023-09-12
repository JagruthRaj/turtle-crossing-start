import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.up,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.createCars()
    car_manager.move_cars()
    


    for stopCars in car_manager.all_cars:
      if stopCars.distance(player)<30:
        game_is_on=False
        scoreboard.Gameover()

    if player.finish():
         player.start_pos()
         car_manager.level_up()
         scoreboard.increase_level()
      
screen.exitonclick()

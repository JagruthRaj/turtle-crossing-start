from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.start_pos()
        self.setheading(90)

    def start_pos(self):
      self.goto(STARTING_POSITION)
      
    def up(self):
      self.penup()
      self.forward(MOVE_DISTANCE)
    
    def finish(self):
      if self.ycor()>FINISH_LINE_Y:
        return True
      else:
        return False
        
    
        
      
      

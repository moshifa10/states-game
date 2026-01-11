from turtle import Turtle

# so in this class that's where I will place every state of Unite state

class StatePlacing(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()


    # do method for turtle to write something in the screen 
    def write_state(self, name_of_state: str, x :int, y :int):
        self.goto(x=x, y=y)
        self.write(
            arg=name_of_state,
            move=True,
            align="center",
            font=("Arial", 8, "normal")
        )

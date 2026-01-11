import turtle as t
import pandas as pd
from states_placing import StatePlacing

# Create a screen 

screen = t.Screen()
screen.bgpic(picname="blank_states_img.gif")


placing_states = StatePlacing()

# planning ->     placing_states.write_state(name_of_state="Arizona", x=-203, y=-40)

# Read csv
data = pd.read_csv("50_state.csv")


screen.exitonclick()
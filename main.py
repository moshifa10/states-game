import turtle as t
import pandas as pd
from states_placing import StatePlacing

# Create a screen 

screen = t.Screen()
screen.bgpic(picname="blank_states_img.gif")


placing_states = StatePlacing()

# planning ->     placing_states.write_state(name_of_state="Arizona", x=-203, y=-40)

# Read csv
data = pd.read_csv("50_states.csv")

# get all coloms and maybe put them into a list then combine 
# I loop in range then create a list of series then use the range to get those 
# I just have to put everything to a dictionary and user so that its easy -> key = state_name, value: (x,y)
states = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()

combine_x_y = list(zip(x_cor,y_cor))

# now just make a dict that will loop with a range
states_with_pos = {}

for index, key  in enumerate(states):
    states_with_pos[key] = combine_x_y[index]

correct = 0
while correct != len(states_with_pos):
    
    # Bring the pop for the user to answer
    user_choice = screen.textinput(title=f"{correct}/{len(states_with_pos)} States/correct", prompt="Enter state:").strip().rstrip().capitalize()

    # Check if the user choice == something in the dict:
    if user_choice in states_with_pos.keys():
        placing_states.write_state(name_of_state=user_choice, x=states_with_pos[user_choice][0], y=states_with_pos[user_choice][1])
        correct += 1

screen.exitonclick()
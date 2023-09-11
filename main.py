import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif" 
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Enter as many State names").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) #or (state.data.state.item())


missing_states = [state for state in all_states if state not in guessed_states]

missing_data = pd.DataFrame(missing_states)

missing_data.to_csv("states_to_learn.csv")
print(missing_data)






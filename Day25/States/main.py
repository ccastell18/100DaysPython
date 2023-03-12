import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
# x_cor = data["x"].to_list()
# y_cor = data["y"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another State's name? ").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # answer.goto(x=x_cor[answer_state], y=y_cor[answer_state])
        state_data = data[data.state == answer_state]
        guessed_states.append(answer_state)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())



pandas.DataFrame


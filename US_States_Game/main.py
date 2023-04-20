import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()

screen.title("US_STATES_GAMES")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

tom = Turtle()
tim = Turtle()
state_data = pandas.read_csv("50_states.csv")

# x = state_data["x"].to_csv("xcor")
# print(state_data)
# print(type(state_data.x))

correct_guesses = []
missing_states = []
points = 0
def read_more():
    for state in state_data.state:
        if state not in correct_guesses:
            missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")


is_game_on = True
while is_game_on and len(correct_guesses) < 5:
    answer_state = screen.textinput(title="Guess the state", prompt="Guess a state in the map below").title()
    chosen_state = state_data[state_data.state == answer_state]

    for state in state_data.state:
         if answer_state == state:
            correct_guesses.append(answer_state)

            # manage score
            points += 1
            tom.hideturtle()
            tom.penup()
            tom.goto(0, 250)
            tom.clear()
            tom.write(arg=f"score:{points}/50", align="center", font=("arial", 9, "normal"))

            #   populate map
            tim.hideturtle()
            tim.penup()
            tim.goto(int(chosen_state.x), int(chosen_state.y))
            tim.write(arg=answer_state, align="center", font=("arial", 9, "normal"))

         elif  answer_state == "exit":
            is_game_on = False
            read_more()
read_more()










    
# def get_mouse_click_coordinates(x, y):
#     print(x, y)#
# turtle.onscreenclick(get_mouse_click_coordinates)
turtle.mainloop()
# screen.exitonclick()

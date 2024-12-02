import turtle
import pandas
screen = turtle.Screen()
screen.title("US states guessing")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

with open("game_data.txt") as data:
    game_data = data.readlines()
guessed_state = []
for i in range(len(game_data)):
    guessed_state.append(game_data[i].strip())

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
is_true = True
tim = turtle.Turtle()
for i in guessed_state:
    score += 1
    states.remove(i)
    x_cor = (data[data["state"] == i].x)
    y_cor = (data[data["state"] == i].y)
    tim.penup()
    tim.goto(int(x_cor), int(y_cor))
    tim.write(i, font=("Arial", 10, "normal"))


while is_true == True:
    user_answer = screen.textinput(
        title=f"{score}/50 Guess the US state.", prompt="Guess next user state.")
    if user_answer in states:
        score += 1
        states.remove(user_answer)
        x_cor = (data[data["state"] == user_answer].x)
        y_cor = (data[data["state"] == user_answer].y)
        tim.penup()
        tim.goto(int(x_cor), int(y_cor))
        tim.write(user_answer, font=("Arial", 10, "normal"))
        with open("game_data.txt", "a") as File:
            File.write(f"{user_answer}\n")
    if score >= 50:
        break
    if user_answer == "off":
        break
    if user_answer == "reset":
        with open("game_data.txt", "w") as File:
            File.write("")
            break


turtle.mainloop()

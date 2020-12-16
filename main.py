import turtle
from titlecase import titlecase
import pandas

data = pandas.read_csv('50_states.csv')

timmy = turtle.Turtle()
timmy.up()
timmy.hideturtle()

screen = turtle.Screen()
screen.title('U.S States Game')
screen.addshape('blank_states_img.gif')

turtle.shape('blank_states_img.gif')
score = 0

while True:
    answer_state = titlecase(screen.textinput(title=f"{score}/50 completed", prompt="What's another state name"))
    name_list = data['state'].tolist()
    guessed_list = []
    not_guessed = []
    if answer_state == 'Exit':
        for i in name_list:
            if i in guessed_list:
                pass
            else:
                not_guessed.append(i)
        pandas.DataFrame({'Missed States':not_guessed}).to_csv('not_guessed.csv')
        break

    elif answer_state in name_list and answer_state not in guessed_list:
        data_coor = (int(data[data['state'] == answer_state].x), int(data[data['state'] == answer_state].y))

        timmy.goto(data_coor)
        timmy.write(answer_state, align='center', font=('Helvetica', 12, 'normal'))
        score += 1
        if score == 50:
            timmy.goto(0, 0)
            timmy.pencolor('green')
            timmy.write('Good Job! You Won!', align='center', font=('Helvetica', 20, 'bold'))
            break
        guessed_list.append(answer_state)
    elif answer_state in name_list and answer_state in guessed_list:
        pass
    else:
        pass


turtle.mainloop()
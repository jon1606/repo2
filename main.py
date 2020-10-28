import random
import stages
import turtle
# import heart
import time
from datetime import datetime
from functools import reduce
import player
from player_factory \
import Player_factory
import webbrowser
logged_in = False

highest_level = 0
factory = Player_factory()
playing_status = 0

print(type(dict))
while playing_status != '1' and playing_status != '2' and playing_status != '3':
    playing_status = input(
        ('Enter:\n 1  - to log in\n 2 -  to sign up \nPress any other button to play as a guest: '))
    if playing_status != '1' and playing_status != '2' and playing_status != '3':
        print('You have to choose one of the options! try again: \n')

if playing_status == '1':
    player = factory.log_in()
    logged_in = True

elif playing_status == '2':
    player = factory.sign_up()
    logged_in = True

#TODO: fix algorithm

#kuku Irina
if logged_in:
    print(f'Your are in class: {player.class_num}')
    print(f'your highest record yet is: {player.level}\n')

else:
    print('Hello geust, welcome to the math game!')
    player = factory.create_player('Geust')
    print('You are starting from level 0...')

player.save()

player.hello()

calc_stage_mark = lambda mistakes_num, exercises_num: 100 - ((100 / exercises_num) * mistakes_num)

report = open(f"player_{player.username}_reports.txt", 'a')
report.write(f'Report for date: {datetime.now()}\n')
report.write('================================================================\n')
report.close()


def reporter(mistakes_dict, player, num_of_exercises):
    report = open(f"player_{player.username}_reports.txt", 'a')
    report.write(f'Step {player.level}: ')
    report.write(
        f'succes rate: {round(calc_stage_mark(len(mistakes_dict), num_of_exercises))}%: {num_of_exercises - len(mistakes_dict)} out of {num_of_exercises}\n')
    report.write('The failures:\n')
    mistake_answers = []
    for exercise, mistakes in mistakes_dict.items():
        mistake_exercise = exercise
        mistake_answers += mistakes
        report.write(f'{mistake_exercise} = {mistake_answers}\n')
    report.write('\n')
    report.close()

    return f'You can find the report on: "player_{player.username}_reports.txt" The report file is called,  find it on your computer '


report = open("mistakes_report.txt", 'r')

report.read()

report.close


def operation(num1=1, num2=2):
    answer = 0
    string_exercise = ''
    operation = random.randint(1, 2)
    if operation == 1:
        answer = num1 + num2
        string_exercise = str(num1) + ' + ' + str(num2)
    elif operation == 2:
        if num1 > num2:
            answer = num1 - num2
            string_exercise = str(num1) + ' - ' + str(num2)
        elif num2 > num1:
            answer = num2 - num1
            string_exercise = str(num2) + ' - ' + str(num1)

    answers = [answer, string_exercise]
    return answers




def f_run_classX_stage(func, player):
    for exercise in range(2):
        nums1 = func()
        answers = operation(nums1[0], nums1[1])
        report_dict = (exercise_proccesor(answers[1], answers[0]))
        print("well done      :)\a\a\a\a\a\a\a\a\a\n")
    print(reporter(report_dict, player, 5))

    return


def dict_proccesor(exercises_dict, player):
    for exercise_string, expected_result in exercises_dict.items():
        report_dict = exercise_proccesor(exercise_string, expected_result)
        print("well done      :)\a\a\a\a\a\a\a\a\a\n")

    print(reporter(report_dict, player, len(exercises_dict)))

    return


mistakes_dict = {}


def exercise_proccesor(exercise, answer):
    is_mistake = False
    user_answer = ''
    # turtle.color('deep pink')
    # style = ('Courier', 30, 'italic')
    # turtle.write(exercise + ' = ', font=style, align='right')
    # turtle.hideturtle()
    try:
        user_answer = int(input(f'how much is {exercise} = '))
    except ValueError:
        print("Sorry, I didn't understand that.")
    # turtle.write(user_answer, font=style, align='left')
    # time.sleep(2)
    user_answers = []
    while user_answer != answer:
        try:
            is_mistake = True
            user_answers.append(user_answer)
            print('Wrong! Try again...   :(  \n\n')
            user_answer = int(input(f'how much is {exercise} = '))
        except ValueError:
            print("Sorry, I didn't understand that.")
        # turtle.write(user_answer, font=style, align='left')
        # time.sleep(1)
    # turtle.clearscreen()
    if is_mistake:
        mistakes_dict[exercise] = user_answers
    return mistakes_dict

classes = {
    1 : [stages.f_class1_stage1,
          stages.f_class1_stage2,
          stages.d_stage3_exercises,
          stages.d_stage4_exercises,
          stages.d_stage5_exercises],
    2 : [stages.f_class2_stage1,
         stages.f_class2_stage2]
}


class1 = [stages.f_class1_stage1,
          stages.f_class1_stage2,
          stages.d_stage3_exercises,
          stages.d_stage4_exercises,
          stages.d_stage5_exercises]

for current_class in range(len(classes) - (player.class_num - 1)):
    for stage in classes[player.class_num]:

            if type(stage) == dict:
                dict_proccesor(stage, player)

            else:
                f_run_classX_stage(stage, player)

            print(f'Well done you finished level: {player.level} !!!!!!!!!')
            player.level += 1
            print(player)

    player.level = 1

    print(f'Your certificate is in this file: "{player.username}_{player.class_num}_certificate"\n')
    if current_class <= len(classes):
        move_class = (input(f"You finished all of the steps in class {player.class_num}! \nWell done!\nType '1' to move to the next class, or any other button to finish: "))
        if move_class != '1':
            print('Thanks for playing in the math game!')
            break
        else:
            player.class_num += 1
            print(f'You are now in class {player.class_num}')
    player.save()

print('You finished all of the classes, you are amazing!')


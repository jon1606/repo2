import random

def f_class1_stage1():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 2)
    nums = [num1, num2]

    return nums


def f_class1_stage2():
    num1 = random.randint(10, 30)
    num2 = random.randint(1, 2)
    nums = [num1, num2]

    return nums


def f_class2_stage1():
    num1 = random.randint(30, 100)
    num2 = random.randint(1, 3)
    nums = [num1, num2]

    return nums


def f_class2_stage2():
    num1 = random.randint(100, 200)
    num2 = random.randint(1, 10)
    nums = [num1, num2]

    return nums


d_stage3_exercises = {
    '10 + 5': 15,
    '15 + 5': 20,
    '20 + 5': 25,
    '25 + 5': 30,
    '40 + 5': 45
}

d_stage4_exercises = {
    '100 + 10': 20,
    '300 + 10': 40,
    '400 + 10': 50,
    '700 + 10': 80
}

d_stage5_exercises = {
    '50 - 2': 48,
    '2 - 2': 0,

    '7 - 6': 1,
    '10 - 9': 1,
    '18 - 17': 1,

    '13 - 3': 10,

    '10 - 10': 0,
    '20 - 20': 0
}
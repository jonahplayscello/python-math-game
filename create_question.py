# I strongly recomend typing this out so Mr.Davis dosen't notice that you are cheating

import random
def create_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer = round(num1 / num2, 2)

    return num1, operator, num2, answer

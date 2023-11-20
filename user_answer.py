# if you haven't done so already import random
def user_answer():
    try:
        user_response = float(input("Your answer: "))
        return user_response
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

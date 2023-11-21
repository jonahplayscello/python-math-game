# I strongly recomend typing this out so Mr.Davis dosen't notice that you are cheating

# this should go after the create_question function 

def user_answer():
    try:
        user_response = float(input("Your answer: "))
        return user_response
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

# I urge you to try and figure this out on your own before using my solution 

# if you do end up using this, be sure to ADD YOUR OWN COMMENTS!


# you will need all of the previous functions to be working and be named correctly for this code function to work

def play_game():
    score = 0
    num_questions = 5

    for _ in range(num_questions):
        number_1, operator, number_2, answer = create_question()
        print(f"what is {number_1} {operator} {number_2}?")

        response = user_answer()

        if response is not None:
            if response == answer:
                print("That's Right\n")
                score += 1
            else:
                print(f"That's not right, The right answer is {answer}\n")
        else:
            print(f"That's not right, The right answer is {answer}\n")

    print(f"You got {score} out of {num_questions}")

# be sure to run play_game() at the end to run the program

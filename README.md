# python-math-game
do not copy and paste this code, write it out manually please

Your assignment is to create a simple math game for grade and middle school students.
Students answer basic math questions + addition,- subtraction,* multiplication, / division
The game asks 5 questions.
The game keeps score 1 for correct and 0 for incorrect.
The questions are randomly generated
first number 1-10
operator +, -, *, /
second number 1-10
For division, you will have to round the computer answer to two decimal places.  1/3=.33 not .33333333333
Your program will have three functions

Function 1 def create_questions()
Determines the first and second number using import random
Determine the operator import random
Returns the answer

Function 2 def user_answer()
User response
Prompt the user for their response to the question
Return True if user_response==answer and false otherwise

Function 3 def_play_game()
Play game
Keep track of score and the number of tries
Tells user if their response is correct or not and their score.

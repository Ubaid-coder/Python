'''
WORKFLOW OF PROJECT
1- Input from user(Rock, paper, scissor)
2- Computer choice (computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock Win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
'''

import random

item_list = ['Rock', 'Paper','Scissor']
user_choice = input('Enter your move = Rock, Paper, Scissor= ').capitalize()
computer_choice= random.choice(item_list)


print(f'User choice = {user_choice}\nComputer choice = {computer_choice}')

if user_choice == computer_choice:
    print("Match Tie")
elif user_choice == 'Rock':
    if computer_choice == 'Paper':
        print('Computer Win')
    else:
        print('You Win')
elif user_choice == 'Paper':
    if computer_choice == 'Scissor':
        print('Computer Win')
    else:
        print('You win')
elif user_choice == 'Scissor':
    if computer_choice == 'Rock':
        print('Computer Win')
    else:
        print('You Win')
else:
    print('Something went wrong')       
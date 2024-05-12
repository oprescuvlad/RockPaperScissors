import random

user_score = 0
ai_score = 0

while True:
    user = input('Please pick one of the following options: rock, paper, scissors\n').lower()
    ai_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f'User picks: {user}')
    print(f'AI picks: {ai_choice}')

    if user == ai_choice:
        print('DRAW')
    elif (user == 'rock' and ai_choice == 'scissors') or \
         (user == 'scissors' and ai_choice == 'paper') or \
         (user == 'paper' and ai_choice == 'rock'):
        print('User wins!')
        user_score += 1
    else:
        print('AI wins!')
        ai_score += 1

    print(f"Score: User - {user_score}, AI - {ai_score}")

    play_again = input('Do you want to play again? (yes/no)\n').lower()
    if play_again != 'yes':
        break

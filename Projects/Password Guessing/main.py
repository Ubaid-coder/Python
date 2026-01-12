import random

easy_words = ['apple', 'tiger', 'train', 'money', 'bus', 'car']
medium_words = ['python', 'bottle', 'chair', 'earth','laptop','mountain']
hard_words = ['diamond', 'bakery', 'medicine', 'doctor', 'geometry','cooker']

print('Welcome to the password gessing game')
print('Choose a difficulty level: easy, medium or hard')

level = input('Enter difficulty: ').lower()

if level == 'easy':
    secret = random.choice(easy_words)
elif level == 'medium':
    secret = random.choice(medium_words)
elif level == 'hard':
    secret = random.choice(hard_words)
else:
    print('Invalid choice. Default to easy level')
    secret = random.choice(easy_words)
    
attempts = 0
print('\nGuess the secret password')

while True:
    guess = input('Enter your guess: ').lower()
    attempts += 1
    
    if guess == secret:
        print(f'Congratulation! You guessed it in {attempts} attempts.')
        break
    hint = ""
    
    for i in range(len(guess)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += '_'
            
        print('Hint: ',hint)

print('GAME END')
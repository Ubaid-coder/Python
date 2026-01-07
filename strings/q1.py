password = input('Enter a password of 5 length: ')
print(len(password))

if len(password) <= 5:
    print('Loggeed In')

else:
    print('password length exceed')
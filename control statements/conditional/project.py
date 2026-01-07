num_1 = float(input('enter number 1 = '))
num_2 = float(input('enter number 2 = '))

choice = input('Enter your choice + - * /: ')

if choice == '+':
    print(num_1 + num_2)
    
elif choice == '-':
    print(num_1 - num_2)
    
elif choice == '*':
    print(num_1 * num_2)
    
elif choice == '/':
    if(num_2 == 0):
        print('can not divide with 0')
        exit()
        
    print(num_1 / num_2)
    
else:
    print('Invalid operation!')
try:
    num1 = int(input('enter number 1: '))
    num2 = int(input('enter number 2: '))
    try:
        result = num1/ num2
        print(f'Result: {result}')
    except ZeroDivisionError:
        print('Can not divide with zero')

except ValueError:
    print('Input must be a number')
    
except:
    print('Something went wrong')
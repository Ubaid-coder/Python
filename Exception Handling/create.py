try:
    num = int(input('enter a number: '))
    result = 10 / num
    print(f'result: {result}')
    
except ZeroDivisionError:
    print('Cannot divide with zero')
    
except ValueError:
    print('Cannot divide with zero')
    
except:
    print('Something went wrong')
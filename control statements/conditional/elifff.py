age = int(input('enter your age = '))
if age>=18:
    print('you can vote!') #True
    
elif age >= 101:
    print('Greater than 101')

elif age<=0:
    print('invalid age')
    
else:
    print('error occurred')
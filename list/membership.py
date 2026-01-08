'''
in - True/False
not in - opposite
'''

list_1 = [1,2,3,4,5]
check = int(input('enter a number to check list: '))

if check in list_1:
    print('Available')

else: 
    print("Not available")
    
if check not in list_1:
    print('yes not found')

else: 
    print("found")
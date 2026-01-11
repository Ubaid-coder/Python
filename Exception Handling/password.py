#check password strength

def check_password(password):
    if len(password) < 8:
       raise  Exception('Password must be 8 characters long')
    
    print('Password is strong')
    

try:
    password = input('enter a password: ')
    check_password(password)
except Exception as err:
    print(err)
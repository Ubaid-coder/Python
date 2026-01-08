'''
burger - function
extra cheese - extra feature

main function> function add
without changin the main funciton code
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper


@my_decorator
def say_hello():
    print('hello')
    
    
say_hello()
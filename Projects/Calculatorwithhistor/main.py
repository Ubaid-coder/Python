HISTORY_FILE = "Projects\Calculatorwithhistor\history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
    
    
def clear_history():
    file = open(HISTORY_FILE,'w')
    file.close()
    print("History Cleared")
    

def save_history(equation, result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "= " + str(result) + "\n")
    file.close()
    

def calculate(user_input):
    part = user_input.split()
    if len(part) != 3:
        print('Invalid input. User format: number operator number  ')
        return
    
    num1 = float(part[0])
    op = part[1]
    num2 = float(part[2])
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print('Can not divide by zero')
            return
        result = num1 / num2
    else:
        print("Invlaid operators. USE ONLY +, -, *, /")
        return
    
    if int(result) == result:
        result = int(result)
        
    print("Result: ",result)
    save_history(user_input, result)
    
    
def main():
    print("----- SIMPLE CALCULATOR (type history,clear or exit )")
    while True:
        user_input = input("Enter calculation  (+ - * / ) or (command history, clear or exit): \n")
        
        if user_input == 'exit':
            print("Good Bye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)


main()
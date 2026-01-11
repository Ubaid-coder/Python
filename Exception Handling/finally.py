try:
    file = open('Exception Handling\errors.txt')
    content = file.read()
    print(content)    

except FileNotFoundError:
    print('File not found')
    
except:
    print('Something went wrong')
    
finally: 
    file.close()
    print(f'file operation completed')
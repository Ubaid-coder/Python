with open('File Handling/file2.txt','w') as file:
    content = input('Enter content to write: ')
    file.write(content)
    print('saved')

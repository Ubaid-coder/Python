with open('File Handling/file2.txt','a') as file:
    content = input('Enter data to append: ')
    file.write(content)
    print('Content Appended')
file = open('File Handling/file2.txt','w')
content = input('Enter a data to write: ')

file.write(content)

print(file)

file.close()
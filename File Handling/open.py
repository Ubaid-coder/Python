'''
open('filename.txt','mode')
'''

file = open('File Handling/file.txt','r')

content = file.read()
print(content)
file.close()
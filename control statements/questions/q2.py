start = int(input('Enter start: '))
stop = int(input('Enter stop: ')) + 1

skip = int(input('Number you want to skip: '))

if start >= stop:
    print('Invalid!')
    exit()

for i in range(start, stop):
    if i == skip:
        continue # ignore that number
    print(i)
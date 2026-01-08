"""
[expression for item in iterable if condition]

e - x*2
item -
iteralbe -range(1,11)
conditional optional
"""

# square = []
# for i in range(1,11):
#     square.append(i**2)
    
# print(square)

squares = [i**2  for i in range(1,11)]
print(squares)
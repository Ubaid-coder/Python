class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
        
student1 = Student("ubaid", 16, 'A+')
student2 = Student("rahim", 17, 'B+')
student3 = Student("shaheer", 18, 'C+')


print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
print(student3.name, student3.age, student3.grade)


'''
1- default constructor (self)
2- parameterized constructor (self, name, age)
3- constructor with default values, (self, name='unknown', age=0)
'''
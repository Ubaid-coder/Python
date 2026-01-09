class Student:
    def set_details(self,name, age):
        self.name = name
        self.age = age


Student1 = Student()
Student1.set_details("ubaid",17)
print(Student1.name, Student1.age)
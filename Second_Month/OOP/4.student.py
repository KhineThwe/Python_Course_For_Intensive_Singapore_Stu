class Student:
    id = 0 #class variable
    name = "Blank" #class variable

    #method
    def introduce(self):
        name = "Khine"#local variable
        id = 1
        print(f'Hello, I am {self.name} with student id {self.id}')

if __name__ == '__main__':
    student = Student()
    # student.id = 2
    # student.name = "KZT"
    student.introduce()
class Student:
    def __init__(self, name : str, age : int, marks : int):
        self.name = name
        self.age = age
        self.marks = marks

    def student_data(self):
        return self.name, self.age, self.marks

class StudentId(Student):
    def __init__(self, id: int, name: str, age: int, marks: int):
        super().__init__(name, age, marks)
        self.id = id


    def student_id(self):
        Student.student_data(self)
        print(f'ID : {self.id} , Name : {self.name} , age : {self.age}, marks : {self.marks}' )

class ParentName(Student):
    def __init__(self, name: str, age: int, marks: int, parent: str):
        super().__init__(name, age, marks)
        self.parent = parent

    def print_parent_info(self):
        Student.student_data(self)
        print(f'Parent Name: {self.parent}, Student Name : {self.name}')

def main():
    print('The students data from class StudentId and Student :')
    student1 = StudentId(1,'Ayush samor', 15, 99)
    student1.student_id()
    print('\n')
    print('The student data from parent and Student : ')
    student2 = ParentName('ANKIT YADAV', 17 , 77, 'RAHUL YADAV')
    student2.print_parent_info()

if __name__ == '__main__':
    main()



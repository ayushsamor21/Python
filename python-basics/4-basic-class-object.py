class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def person_info(self):
        print(f'Person Info : {self.name}, {self.age}')


def main():
    person1 = Person('ayush samor', 45)
    person1.person_info()

    person2 = Person('rajveer singh', 98)
    person2.person_info()

if __name__ == '__main__':
     main()

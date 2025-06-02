import json

def read_file(file_name):
    with open(file_name, 'r') as file:
        student = json.load(file)    # load converts to python <class 'dict'>
        print(type(student))
        print(student)
        for row in student:
            print("Name:", row["NAME"])
            print("State:", row["STATE"])
            print("Grade:", row["GRADE"])
            print("Class:", row["CLASS"])
            print('------------')

def main():
    file_name = 'student_data.json'
    read_file(file_name)

if __name__ == '__main__':
    main()

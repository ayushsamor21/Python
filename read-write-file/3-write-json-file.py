import json

students = [
    {
        "NAME": "AYUSH SAMOR",
        "STATE": "DELHI",
        "GRADE": 89,
        "CLASS": "12TH"
    },
    {
        "NAME": "RAJVEER SINGH",
        "STATE": "RAJASTHAN",
        "GRADE": 99,
        "CLASS": "12TH"
    },
    {
        "NAME": "ANANYA SING",
        "STATE": "MP",
        "GRADE": 87,
        "CLASS": "12TH"
    }
]

def write_file(file_name):
    with open(file_name, 'w') as file:
        json.dump(students, file, indent=4)

def main():
    file_name = 'read_student_data.json'
    write_file(file_name)
if __name__ == '__main__':
    main()

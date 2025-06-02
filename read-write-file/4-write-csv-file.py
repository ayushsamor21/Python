import csv

students = [
    ["NAME", "STATE", "MARKS", "CLASS"],
    ["AYUSH SAMOR", "DELHI", 89, "12TH"],
    ["RAJVEER SINGH", "RAJASTHAN", 99, "12TH"],
    ["ANANYA SINGH", "MP", 87, "12TH"]
]

def write_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)

def main():
    file_name = 'read_student_data.csv'
    write_file(file_name)

if __name__ == '__main__':
    main()

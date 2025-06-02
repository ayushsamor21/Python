import csv

def read_file(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        print(reader)   #<csv.DictReader object at "memory_location">
        for row in reader:
            print("Name:", row["NAME"])
            print("State:", row["STATE"])
            print("Grade:", row["MARKS"])
            print("Class:", row["GRADE"])
            print("---------------------")

def main():
    file_name = 'student_data.csv'
    read_file(file_name)

if __name__ == '__main__':
    main()

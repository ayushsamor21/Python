def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("THIS IS TEST RUN\n")
        file.write("HELLO\n")


def read_file(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        print(content)

def main():
    file_name = 'ayush.txt'
    create_file(file_name)
    read_file(file_name)

if __name__ == '__main__':
    main()
  

def main():
    filename = "student_data.json"
    alist = filename.split(".")
    print(f'the List : {alist}')
    print('The length of the list : ', len(alist))
    print(alist[len(alist) - 1])   #method - 1
    print(alist[-1])               #method - 2

if __name__ == '__main__':
    main()

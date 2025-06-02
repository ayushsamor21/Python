# List : ordered, changeable , allows duplicate
nameList = ['RAJVEER', 'AYUSH', 'RUDRA']
print(nameList)

#len command
numberList = [23, 55, 645, 64, 23, 56]
print(numberList)
print(f'THE length of the array :{len(numberList)}')

#type
list1 = [12, "RAJVEER", False, 13, "RUDRA", True]
print(type(list1))

#list() constructor
list_constructor =  list((12, 45, 62, 51, 45, 90))
print(list_constructor)

size = len(nameList)
print('\nPrinting using For loop:')
for index in range(size):
    print(f'index[{index}] : {nameList[index]}')

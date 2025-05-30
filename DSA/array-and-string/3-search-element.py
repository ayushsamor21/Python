size = int(input('Please enter the size of the array : '))
array = []

for i in range(size):
    num = int(input(f'Please enter the element at index [{i}] : '))
    array.append(num)

search_element = int(input('Please enter the element you want to search : '))

occurrence = False
for i in range(size):
    if array[i] == search_element:
        occurrence = True
        break

if occurrence:
    print(f'The element {search_element} is present in the array ')
else:
    print(f'The element {search_element} is not present in the array ')

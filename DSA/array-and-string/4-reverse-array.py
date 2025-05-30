size = int(input('Please enter the size of the array : '))
arr1 = []
arr2 = []

for i in range(size):
    num = int(input(f'Please enter the array at index [{i}] : '))
    arr1.append(num)

for i in range(size - 1, -1, -1):
    arr2.append(arr1[i])

print('Original array :', arr1)
print('Reversed array :', arr2)

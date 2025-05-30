size = int(input('Please enter the size of array : '))
array = []

for i in range(size):
    num = int(input(f'Please enter the array at index [{i}] : '))
    array.append(num)

#even index
print('Even index array elements : ')
for i in range(size):
    if i % 2 == 0:
        print(f'index[{i}] : ', array[i])

print('\n')
#odd index
print('Odd index array elements : ')
for i in range(size):
    if i % 2 != 0:
        print(f'index[{i}] : ', array[i])

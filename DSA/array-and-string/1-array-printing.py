size = int(input("Enter the size of the array: "))
array = []

for i in range(size):
    num = int(input(f'Please enter the number at index [{i}] : '))  #f'..' :formatted string literal , for variable inside string 
    array.append(num) #append to add num 

print('Entered array :')
print(array)

print ('--Please choose the number from list of operations--')
print('1.Addition\n2.Subtraction\n3.multiplication\n4.division')
num1 = int(input('Please enter number 1 : '))
num2 = int(input('Please enter number 2 : '))
operations = int(input('Please enter the operation  : '))
match operations:
    case 1 :
        sum1 = num1 + num2
        print('The sum :', sum1)

    case 2 :
        sub1 = num1 - num2
        print('The difference :', sub1)

    case 3 :
        multi1 = num1 * num2
        print('The product :', multi1)

    case 4  if num1 != 0 and num2 != 0:
        div1 = num1 / num2
        print('The division  :', div1)

    case _:
        print('please choose the valid number .')

#case 1 | 2 | 3 | 4 can also be used in match

def func(num1, num2):
    if num1 == 65 or num2 == 65:
        print(True)
    elif num1 + num2 == 65:
        print(True)
    else:
        print(False)

num1 = int(input('Enter number:'))
num2 = int(input('Enter another number:'))
func(num1, num2)          

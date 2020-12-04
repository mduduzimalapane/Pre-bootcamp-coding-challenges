def func(num1, num2):
    if num1 == 65 or num2 == 65:
        return True
    elif num1 + num2 == 65:
        return True
    else:
        return False

num1 = int(input('Enter number:'))
num2 = int(input('Enter another number:'))
func(num1, num2)          

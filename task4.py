def func(num1, num2):
    if num1 == 3 or num2 == 3:
        numb = num1 + num2
        if '3' in str(numb):
            print(True) 
        else:
            print(False)

num1 = int(input('Enter number:'))
num2 = int(input('Enter another number:'))
func(num1, num2)        


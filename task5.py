import math

def func(num1, num2, num3):
    s = 0.5 * (num1 + num2 + num3)
    a = math.sqrt(s * (s - num1) * (s - num2) * (s - num3))
    print(a)

num1 = int(input('Enter number:'))
num2 = int(input('Enter another number:'))
num3 = int(input('And another one:'))
func(num1, num2, num3)

def func(num1, num2, num3):
    s = (num1 + num2 + num3) / 2
    a = (s * (s - num1) * (s - num2) * (s - num3)) ** 0.5
    print(a)

num1 = float(input('Enter side:'))
num2 = float(input('Enter another side:'))
num3 = float(input('And another side:'))
func(num1, num2, num3)
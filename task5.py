
def area_of_triangle(num1, num2, num3):
    s = (num1 + num2 + num3) / 2
    a = (s * (s - num1) * (s - num2) * (s - num3)) ** 0.5
    return a

area_of_triangle(3, 4, 5)

def area_of_triangle(num1, num2, num3):
    semi_parameter = (num1 + num2 + num3) / 2
    area = (semi_parameter * (semi_parameter - num1) * (semi_parameter - num2) * (semi_parameter - num3)) ** 0.5
    return area

area_of_triangle(3, 4, 5)
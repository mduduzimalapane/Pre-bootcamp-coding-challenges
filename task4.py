def sum_of(num1, num2):
    if num1 == 3 or num2 == 3:
        numb = num1 + num2
        if '3' in str(numb):
            return True 
        else:
            return False
    else:
        return False     

sum_of(35, 3)        


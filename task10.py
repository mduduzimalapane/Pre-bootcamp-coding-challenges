def func(string):
    for i in 'aeiou':
        if i in string.lower():
            print(i)

string =  input('Enter something:')
func(string)
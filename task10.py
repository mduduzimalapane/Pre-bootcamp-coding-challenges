def func(string):
    for i in 'aeiouAEIOU':
        if i in string:
            print(i)

string =  input('Enter something:')
func(string)
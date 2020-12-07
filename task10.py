def vowels(string):
    for i in 'aeiouAEIOU':
        if i in string:
            print(i)

string =  input('Enter something:')
vowels(string)
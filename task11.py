def func(str1, str2):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in str1 and i in str2:
            print(i)

str1 = input('Enter a word:')
str2 = input('Enter another word:') 
func(str1, str2)          
def common_characters(str1, str2):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in str1 and i in str2:
            print(i, end=" ")


str1 = input('Enter a word:')
str2 = input('Enter another word:') 
common_characters(str1, str2)          
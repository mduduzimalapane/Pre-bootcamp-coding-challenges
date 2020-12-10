
def common_characters(str1, str2):
    common = []
    if len(str1) < len(str2):
        for char in str1:
            if char in str2:
                common.append(char)
    else:
        for char in str2:
            if char in str1:
                common.append(char)
    print('Common letters:', *common, sep=',')


str1 = input('Enter a word:')
str2 = input('Enter another word:') 
common_characters(str1, str2)  

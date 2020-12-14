def common_characters(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    common = []
    for char in str1:
        if char in str2:
            common.append(char)
    print('Common letters:', ', '.join(common))

common_characters('house', 'computer')

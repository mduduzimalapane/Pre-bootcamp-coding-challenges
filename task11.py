
def common_characters(str1='resolve', str2='relaxation'):
    common = []
    if len(str1) > len(str2):
        for char in str1:
            if char in str2:
                common.append(char)
    else:
        for char in str2:
            if char in str1:
                common.append(char)
    print('Common letters:', *common, sep=',')


common_characters()  

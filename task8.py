def hours_and_minutes(minutes):
    hrs = minutes / 60
    minutes = minutes % 60
    hrs = int(hrs)
    if hrs > 1 and minutes > 1:
        print(f'{hrs} hours, {minutes} minutes')
    elif hrs > 1 and minutes == 1:
        print(f'{hrs} hours, {minute} minute')
    elif hrs == 1 and minutes > 1:
        print(f'{hrs} hour, {minutes} minutes')    
    elif hrs == 1 and minutes == 1:
        print(f'{hrs} hour, {minutes} minute') 
    else:     
        print(f'{hrs} hours, {minutes} minutes')     

hours_and_minutes(0)
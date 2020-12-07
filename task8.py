def hours_and_minutes(minutes):
    hrs = minutes / 60
    minutes = minutes % 60
    hrs = int(hrs)
    print(f'{hrs} hours, {minutes} minutes')
  
hours_and_minutes(133)
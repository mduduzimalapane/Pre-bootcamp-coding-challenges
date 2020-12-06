def func(minutes):
    hrs = minutes / 60
    minutes = minutes % 60
    hrs = int(hrs)
    print(f'{hrs} hours {minutes} minutes')
  
func(71)
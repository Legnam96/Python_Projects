def add_time(start, duration, day=False):

  days_of_the_week_hm = {
   'Monday':0, 'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':'4', 'Saturday':5,'Sunday':6 }
  days_of_the_week_array = [
   "Monday"
  ,"Tuesday"
  ,"Wednesday"
  ,"Thursday"
  ,"Friday"
  ,"Saturday"
  ,"Sunday" ]
   
  start_hours = int(start.split(':')[0])
  start_minutes = int(start.split(':')[1][0:2])
  am_or_pm = str(start.split(' ')[1])
  duration_hours = int(duration.split(':')[0])
  duration_minutes = int(duration.split(':')[1])
  am_to_pm = {"AM":"PM", "PM":"AM"}
  number_of_days = (duration_hours//24)
  
  end_minutes = start_minutes+duration_minutes
  if end_minutes >= 60:
    start_hours += 1
    end_minutes = end_minutes % 60
  number_of_am_to_pm = ((start_hours+duration_hours)//12)
  end_hours = (start_hours+duration_hours) % 12
    
  end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
  end_hours = end_hours = 12 if end_hours == 0 else end_hours
  if(am_or_pm == "PM" and start_hours + (duration_hours%12) >= 12):
    number_of_days += 1


  am_or_pm = am_to_pm[am_or_pm] if number_of_am_to_pm % 2 == 1 else am_or_pm
  new_time = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm 
  if(day):
    day = day.capitalize()
    index = int((days_of_the_week_hm[day]) + number_of_days) % 7
    new_day = days_of_the_week_array[index]
    new_time += ", " + new_day

  if (number_of_days == 1):
    return new_time + " " + "(next day)"
  elif(number_of_days >1): 
    return new_time + " (" + str(number_of_days) + " days later)"
  
  return new_time
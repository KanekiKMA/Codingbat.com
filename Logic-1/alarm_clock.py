def alarm_clock(day, vacation):
  if(not vacation and day>0 and day<6):
    return "7:00"
  elif((not vacation and(day==0 or day==6)) or (vacation and day>0 and day<6)):
    return "10:00"
  else:
    return "off"

def caught_speeding(speed, is_birthday):
  if((not is_birthday and speed<=60)or(is_birthday and speed<=65)):
    return 0
  elif((not is_birthday and speed<=80)or (is_birthday and speed<=85)):
    return 1
  else:
    return 2
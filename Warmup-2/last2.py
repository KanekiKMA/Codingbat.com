def last2(str):
  if len(str)<2:
    return 0
  count=0
  for i in range(len(str)-2):
    if str[i:i+2]==str[len(str)-2:len(str)]:
      count+=1
  return count
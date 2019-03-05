def string_match(a, b):
  count=0
  leng=len(a)
  if len(a)>len(b):
    leng=len(b)
  for i in range(leng-1):
    if a[i:i+2]==b[i:i+2]:
      count+=1
  return count
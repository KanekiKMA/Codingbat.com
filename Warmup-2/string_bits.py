def string_bits(str):
  str1=""
  i=0
  while(i<len(str)):
    str1+=str[i:i+1]
    i+=2
  return str1
def combo_string(a, b):
  shorter=a
  longer=b
  if(len(a)>len(b)):
    shorter=b
    longer=a
  return shorter+longer+shorter

def not_string(str):
  if('not' in str[:3]):
    return str
  else:
    return 'not ' + str
def not_string(str):
  if str.split(' ')[0] == 'not':
    return str
  else:
    return 'not ' + str
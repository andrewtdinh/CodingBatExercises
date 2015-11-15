def last2(str):
  if len(str) < 3:
    return 0
  else:
    return len([str[i:(i+2)] for i in range(len(str) - 1) if str[i:(i+2)]==str[-2:]]) - 1

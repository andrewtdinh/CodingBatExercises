def missing_char(str, n):
  if n == len(str) - 1:
    return str[:n]
  else:
    return str[:n] + str[(n + 1):]
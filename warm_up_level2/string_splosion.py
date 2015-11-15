def string_splosion(str):
  return ''.join([str[:(i + 1)] for i, ch in enumerate(list(str))])

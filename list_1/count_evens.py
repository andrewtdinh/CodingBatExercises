def count_evens(nums):
  evens = [1 for num in nums if num % 2 == 0]
  return reduce(lambda x, y: x + y, evens)

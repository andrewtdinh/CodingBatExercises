def count_evens(nums):
  evens = [1 for num in nums if num % 2 == 0]
  print evens
  return reduce(lambda x, y: x + y, evens)

count_evens([3,5,2,4, 6])

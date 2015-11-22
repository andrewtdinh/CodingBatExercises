def centered_average(nums):
  nums.sort()
  return reduce(lambda x,y: x+y, nums[1:-1]) / len(nums[1:-1])

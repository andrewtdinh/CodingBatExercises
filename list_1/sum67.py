def sum67(nums):
  next6 = nums.find(6)
  while (next6 and nums.find(7, next6)):
    del nums[next6:nums.find(7, next6)]
    next6 = nums.find(6)
  return nums

arr = [1, 3, 5, 6, 3, 5, 6, 7]

def sum67(nums):
  while (6 in nums and 7 in nums[nums.index(6):]):
    index7 = nums[nums.index(6):].index(7)
    del nums[nums.index(6):index7 + 1]
  return sum(nums)

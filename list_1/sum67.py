def sum67(nums):
  while ((6 in nums and 7 in nums) and (nums.index(6) < nums.index(7))):
    del nums[nums.index(6):nums.index(7) + 1]
  return sum(nums)

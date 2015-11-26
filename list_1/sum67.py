def sum67(nums):
  while 6 in nums and 7 in nums[nums.index(6):]:
    index6 = nums.index(6)
    index7 = nums[index6:].index(7) + index6
    nums = nums[:index6] + nums[(index7 + 1):]
  return sum(nums)

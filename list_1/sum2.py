def sum2(nums):
  if len(nums):
    if len(nums) >= 2:
      return nums[0] + nums[1]
    else:
      return nums[0]
  else:
    return 0

def sum13(nums):
  if nums:
    blackList = [i for i in range(len(nums)) if nums[i] == 13] + [i + 1 for i in range(len(nums)) if nums[i] == 13]
    if blackList:
      return sum([nums[i] for i in range(len(nums)) if i not in blackList])
    else:
      return sum(nums)
  else:
    return 0

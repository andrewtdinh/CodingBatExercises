def sum13(nums):
  if nums:
    indicesOf13 = [i for i in range(len(nums)) if nums[i] == 13]
    blackList = indicesOf13 + [indx + 1 for indx in indicesOf13]
    if indicesOf13:
      return sum([nums[i] for i in range(len(nums)) if i not in blackList])
    else:
      return sum(nums)
  else:
    return 0

def sum67(nums):
  arr_length = len(nums)
  indices_6 = [i for i in range(arr_length) if nums[i]==6]
  indices_7 = [i for i in range(arr_length) if nums[i]==7]
  for index, startPos in enumerate(indices_6):
    nums = nums[:startPos] + nums[indices_7[index] + 1:]
  return nums
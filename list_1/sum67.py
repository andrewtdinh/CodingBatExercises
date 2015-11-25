def sum67(nums):
  arr_length = len(nums)
  indices_7 = [i for i in range(arr_length) if nums[i]==7]
  indices_6 = [i for i in range(arr_length) if nums[i]==6]
  indices_6 = indices_6[:len(indices_7)]
  for index, startPos in enumerate(indices_6):
    del nums[startPos:indices_7[index] + 1]
  return nums
  
arr = [1, 3, 5, 6, 3, 5, 6, 7]
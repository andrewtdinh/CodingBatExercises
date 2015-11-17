def max_end3(nums):
  return [nums[0] if nums[0] > nums[-1] else nums[-1] for num in nums]
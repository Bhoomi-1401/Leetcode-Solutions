class Solution:
    def twoSum(self, nums, target):
        memory = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in memory:
                return [memory[needed], i]
            else:
                memory[nums[i]] = i
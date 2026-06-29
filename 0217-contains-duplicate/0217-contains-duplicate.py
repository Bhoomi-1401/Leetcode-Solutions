class Solution(object):
    def containsDuplicate(self, nums):
        memory = set()
        for i in range(len(nums)):
            if nums[i] in memory:
                return True
            else:
                memory.add(nums[i])
        return False

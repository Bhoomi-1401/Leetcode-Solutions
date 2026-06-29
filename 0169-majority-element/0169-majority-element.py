class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 1
        n = len(nums)
        for i in range(len(nums)):
            if count[nums[i]] > n/2:
                return nums[i]


        
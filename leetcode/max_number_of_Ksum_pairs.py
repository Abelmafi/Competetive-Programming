class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        start = 0
        end = len(nums) - 1
        counter = 0
        while start < end:
            if nums[start] + nums[end] > k:
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
            else:
                start += 1
                end -= 1
                counter += 1
        return counter

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        nums.sort()
        max_num = nums[0]
        while start < end:
            sum = nums[start] + nums[end]
            if sum > max_num:
                max_num = sum
            start += 1
            end -= 1
        return max_num

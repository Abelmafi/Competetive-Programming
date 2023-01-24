class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums = [int(i) for i in nums]
        nums.sort()
        return str(nums[len(nums) - k])

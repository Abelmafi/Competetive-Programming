class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        if n == 1:
            return str(nums[0])
        nums = [str(i) for i in nums]
        for i in range(n):
            for j in range(1 + i, n):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        result = "".join(nums)
        if int(result) == 0:
            return "0"
        return result

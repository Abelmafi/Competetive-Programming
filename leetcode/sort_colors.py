class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        swapped = False
        result = []
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    swapped = True
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            if not swapped:
                break
        return nums

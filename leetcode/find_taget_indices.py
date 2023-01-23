class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
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
        for i, v in enumerate(nums):
            if v == target:
                result.append(i)
        return result

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums) - 1) :
                if (nums[i - 1] + nums[i + 1]) / 2 == nums[i]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        for i in range(1, len(nums) - 1) :
            if (nums[i - 1] + nums[i + 1]) / 2 == nums[i]:
                self.rearrangeArray(nums)

        return nums

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i, v in enumerate(nums):
            count = 0
            for j in nums:
                if v > j:
                    count += 1
            result.append(count)
        return result

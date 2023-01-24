class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        n = len(l)
        result = []
        q_list = []
        for i in range(n):
            q_list = nums[l[i]:r[i] + 1]
            q_list.sort()
            flag = True
            gap = q_list[1] - q_list[0]
            for j in range(len(q_list) - 1):
                if q_list[j + 1] - q_list[j] != gap:
                    flag = False
                    break
            result.append(flag)
        return result

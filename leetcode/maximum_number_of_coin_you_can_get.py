class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        chances = len(piles) / 3
        piles.sort(reverse=True)
        count = 0
        index = 1
        while chances > 0:
            count += piles[index]
            chances -= 1
            index += 2 
        return count

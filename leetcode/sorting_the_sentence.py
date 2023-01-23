class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words_list = s.split(' ')
        result = ['' for i in range(len(words_list))]
            
        for i in words_list:
            order = int(i[-1])
            result[order - 1] = i[0:-1]
        return (' '.join(result))

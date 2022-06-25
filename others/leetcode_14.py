class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp = []
        
        for i in range(1,len(strs)):

            for j in range(len(min(strs, key=len))):

                criterion = strs[0][j]

                if strs[i][j] != criterion:
                    break

                



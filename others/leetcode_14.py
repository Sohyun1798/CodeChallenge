from curses.ascii import SO


class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        criterion = min(strs, key=len)

        if len(strs) == 1 or criterion=="":

            return criterion

        else:
            
            for j in range(len(criterion)):
                for i in range(1, len(strs)):
                    temp = strs[0][j]
                   
                    if strs[i][j] != temp:
                        temp = ""
                        break
                    
                if temp != "":
                    answer += temp

                else:
                    break
                    
            return answer

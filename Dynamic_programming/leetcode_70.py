

class Solution(object):

    dp = [0] * 46 # setting as global variable for solution2

    def climbStairs(self, n):
        if n<=2: return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        elif self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs2(n-1) + self.climbStairs2(n-2)
        return self.dp[n]
            



        return 
        

S = Solution()
print(S.climbStairs(3))




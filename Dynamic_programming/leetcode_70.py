class Solution(object):

    def climbStairs(self, n):
        if n<=2: return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]


    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        count = self.basicFunc(n, count)

        return count

    def basicFunc(self, m, count):

        if m == 0:
            return count
        elif m < 0:
            return 0

        return self.basicFunc(m-1, count+1), self.basicFunc(m-2, count+1)
        

S = Solution()
print(S.climbStairs(3))




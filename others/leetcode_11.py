#improved brute force

class Solution(object):
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        Max = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):

                v = min(height[i], height[j])
                h = j-i

                if v*h > Max:

                    Max = v*h

        return Max

class Solution2:
    def maxArea(self, height: List[int]) -> int:
        
        left=0
        right=len(height)-1
        max_area=0
        while (right-left>0) :
            max_area=max(max_area,(right-left)*min(height[left],height[right]))
                
            if height[left]>=height[right]: # The right is shorter than left
                right-=1
            else: # The left is shorter than right
                left+=1
            
        return max_area

height = [1,1]
print(Solution.maxArea(height))
                


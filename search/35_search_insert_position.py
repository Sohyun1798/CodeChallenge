# 39ms, 14.2MB

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = 0
        
        if nums[len(nums)-1] < target:
            answer = len(nums)
            
        else:
            for i in range(len(nums)):
                
                if nums[i] >= target:
                    answer = i
                    break
        
        return answer
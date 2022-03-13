# 98ms, 16.1MB

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        idx = len(nums)/2
        root = TreeNode(val=nums[idx])
        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[idx+1:])
            
        return root
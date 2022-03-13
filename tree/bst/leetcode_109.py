# 132ms, 25.6MB

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
  
    def nodeListToList(self, ListNode):
        tempList = []
        
        if not ListNode:
            return tempList
        
        while ListNode:
            tempList.append(ListNode.val)
            ListNode = ListNode.next
            
        return tempList
    
    def BST(self, List):
        
        if not List:
            return None
        
        idx = len(List)/2
        
        root = TreeNode(val=List[idx])
        root.left = self.BST(List[:idx])
        root.right = self.BST(List[idx+1:])
        
        return root
        
    
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        temp = self.nodeListToList(head)
        
        return self.BST(temp)
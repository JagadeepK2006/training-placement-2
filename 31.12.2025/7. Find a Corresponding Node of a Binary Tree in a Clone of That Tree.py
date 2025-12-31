class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if not original:
            return None
        if original == target:
            return cloned
        left = self.getTargetCopy(original.left,cloned.left,target)
        if left:
            return left
        return self.getTargetCopy(original.right,cloned.right,target)
        

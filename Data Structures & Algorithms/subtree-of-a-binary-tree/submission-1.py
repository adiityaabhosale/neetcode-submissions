class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Base cases: empty root cannot contain a subtree; if identical, return True
        if not root: return False
        if self.isSameTree(root, subRoot): return True
        
        # Look for subRoot in the left or right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is q: return True
        return bool(p and q and p.val == q.val and 
                    self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))

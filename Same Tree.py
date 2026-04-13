# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        # Base Case 2: One node is None, the other isn't
        if not p or not q:
            return False

        # Base Case 3: Node values are different
        if p.val != q.val:
            return False

        # Recursive Case: Check left subtrees AND right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

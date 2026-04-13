# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        def p0(root):
            if root == None : return
            p0(root.left)
            p0(root.right)
            ans.append(root.val)
        p0(root)
        return ans
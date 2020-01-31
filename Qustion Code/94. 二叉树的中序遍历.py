# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res

    def helper(self,root,res):
        if root != None:
            if root.left != None:
                self.helper(root.left,res)
            res.append(root.val)
            if root.right != None:
                self.helper(root.right,res)
        return res
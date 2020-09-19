# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def helper(node,flag):
            nonlocal res
            if not node.left and not node.right and flag:
                res = res + node.val
            if node.left:
                helper(node.left,1)
            if node.right:
                helper(node.right,0)
            return            
        res = 0
        if root:
            helper(root,0)
        return res

# method_1.1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res 
        if root.left and not root.left.left and not root.left.right:
            res = root.left.val
        return res + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

# method_2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
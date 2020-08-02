# method_1.1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        queue = []
        def helper(node):
            if node:
                queue.append(node)
                helper(node.left)
                helper(node.right)
        
        helper(root)

        for i in range(len(queue)-1):
            queue[i].right  = queue[i+1]
            queue[i].left = None

# method_1.2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return 
        queue = []
        stack = [root]
        while stack:
            node = stack.pop()
            queue.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        for i in range(len(queue)-1):
            queue[i].right  = queue[i+1]
            queue[i].left = None

# method_2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        stack = [root]
        prev = None
        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            prev = curr


# method_3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                pre = nxt = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.right = nxt
                curr.left = None 
            curr = curr.right


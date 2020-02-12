# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float('-inf'))

        def in_order(node):
            if not node:
                return
            # 中序遍历
            in_order(node.left)

            if not self.firstNode and self.preNode.val >= node.val:
                self.firstNode = self.preNode
            if self.firstNode and self.preNode.val >= node.val:
                self.secondNode = node
            self.preNode = node
            in_order(node.right)
        
        in_order(root)
        self.firstNode.val,self.secondNode.val = self.secondNode.val,self.firstNode.val
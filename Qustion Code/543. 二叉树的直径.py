# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        self.depth(root)
        # 路径节点数减一
        return self.ans - 1

    def depth(self, node):
        if node == None:
            return 0
        # 左儿子的深度：
        L = self.depth(node.left)
        # 右儿子的深度
        R = self.depth(node.right)
        # 当前节点的深度
        cur_depth = L+R+1
        # 更新ans
        self.ans = max(self.ans,cur_depth)
        return max(L,R) + 1
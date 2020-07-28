# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        else:
            return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)

# method_2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        ans = 0
        q = [root]
        while q:
            # 当前层的节点数
            sz = len(q)
            while sz > 0:
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                sz -= 1
            ans += 1


        return ans  
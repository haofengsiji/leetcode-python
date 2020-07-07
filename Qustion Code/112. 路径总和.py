# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, Sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return Sum == root.val
        return self.hasPathSum(root.left,Sum - root.val) or self.hasPathSum(root.right,Sum - root.val)

# method_2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, Sum: int) -> bool:
        q = collections.deque()
        cur = collections.deque()
        if not root: return False
        q.append(root)
        cur.append(root.val)
        while q:
            node = q.popleft()
            val = cur.popleft()
            if not node.left and not node.right:
                if val == Sum:
                    return True
                continue
            if node.left:
                q.append(node.left)
                cur.append(val+node.left.val)
            if node.right:
                q.append(node.right)
                cur.append(val+node.right.val)
        return False
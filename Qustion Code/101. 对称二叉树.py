# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    
    def isMirror(self,t1,t2):
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False
        else:
            return t1.val == t2.val \
                and self.isMirror(t1.left,t2.right) \
                and self.isMirror(t1.right,t2.left)

# method_2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = collections.deque()
        q.append((root,root))
        while q:
            t1,t2 = q.pop()
            if t1 == None and t2 == None:
                continue
            elif t1 == None or t2 == None:
                return False
            elif t1.val != t2.val:
                return False
            q.append((t1.left,t2.right))
            q.append((t1.right,t2.left))
        return True
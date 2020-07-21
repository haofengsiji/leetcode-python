# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(start,end):
            if start > end: return [None]
            treeList = []
            for i in range(start, end+1):

                treeLeft = helper(start,i-1)
                treeRight = helper(i+1,end)

                for left in treeLeft:
                    for right in treeRight:
                        curTree = TreeNode(i)
                        curTree.left = left
                        curTree.right = right   
                        treeList.append(curTree)
            
            return treeList
        
        return helper(1,n) if n else []

# method_2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        memo = [[None]*n for _ in range(n)]

        def helper(start,end):
            if start > end: return [None]
            if memo[start-1][end-1]: return memo[start-1][end-1]

            treeList = []
            for i in range(start, end+1):

                treeLeft = helper(start,i-1)
                treeRight = helper(i+1,end)

                for left in treeLeft:
                    for right in treeRight:
                        curTree = TreeNode(i)
                        curTree.left = left
                        curTree.right = right   
                        treeList.append(curTree)
            
            memo[start-1][end-1] = treeList

            return treeList
        
        return helper(1,n) if n else []
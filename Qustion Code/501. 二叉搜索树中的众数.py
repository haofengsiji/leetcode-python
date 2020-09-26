# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:return []
        def helper(node):
            if not node: return 
            count[node.val] = count.setdefault(node.val,0) + 1
            helper(node.left)
            helper(node.right)
        
        count = dict()
        helper(root)
        count = sorted(count.items(),key=lambda x:x[1],reverse=True)
        res = []
        res.append(count[0][0])
        for i in range(1,len(count)):
            if count[i][1] == count[0][1]:
                res.append(count[i][0])
        return res
        

# method_2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        def searchBST(cur):
            if not cur: return 
            nonlocal pre,count,res,maxCount
            searchBST(cur.left)
            if pre == None:
                count += 1
            elif pre.val == cur.val:
                count += 1
            else:
                count = 1
            pre = cur
            if count == maxCount:
                res.append(cur.val)
            if count > maxCount:
                maxCount = count
                res = []
                res.append(cur.val)
            searchBST(cur.right)
            return
        
        count = 0
        maxCount = 0
        res = []
        pre = None
        searchBST(root)
        return res
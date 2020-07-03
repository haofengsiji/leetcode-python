# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left,right):
            if left > right: return None

            mid = (left+right)//2
            node = TreeNode(nums[mid])
            node.left = helper(left,mid-1)
            node.right = helper(mid+1,right)
        
            return node

        return helper(0,len(nums)-1)
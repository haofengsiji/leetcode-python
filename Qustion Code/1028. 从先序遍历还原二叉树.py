# method_1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path = list()
        i = 0
        while i < len(S):
            # 统计当前level
            level = 0
            while S[i] == '-':
                level += 1
                i += 1

            # 字符转化
            val = 0
            while i < len(S) and S[i].isdigit():
                val = val*10 + ord(S[i])-ord('0')
                i += 1
            
            # 构建节点
            node = TreeNode(val)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)

        return path[0]   

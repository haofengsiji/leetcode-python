# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None: return 'X,'
        leftserilized = self.serialize(root.left)
        rightserilized = self.serialize(root.right)
        return str(root.val) + ',' + leftserilized + rightserilized

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        root = self.buildTree(data)
        return root 

    
    def buildTree(self,data):
        if not data: return None
        val = data.pop(0)
        if val == 'X': return None
        node = TreeNode(val)
        node.left = self.buildTree(data)
        node.right = self.buildTree(data)
        return node

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
                path[-1].right = TreeNode(val)
            path.append(node)

        return path[0] 

if __name__ == "__main__":
    s = Solution()
    c = Codec()
    print(c.serialize(s.recoverFromPreorder("1-2--3--4-5--6--7")))
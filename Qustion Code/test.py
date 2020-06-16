# Definition for a binary tree node.

class TreeNode(object):
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

                    





 

if __name__ == "__main__":
    s = Codec()
    root = s.deserialize('1,2,3,X,X,4,5')
    print(s.serialize(root))

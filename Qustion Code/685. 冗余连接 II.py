# method_1
class UnionFind:
    def __init__(self,n):
        self.ancestor = list(range(n))
    
    def union(self, index1:int, index2:int):
        root1 = self.find(index1)
        root2 = self.find(index2)

        if root1 == root2:
            return False
        self.ancestor[index1] = root2
        return True

    def find(self, index:int)->int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # 边的条数
        numEdges = len(edges)
        # 步骤1，预处理入读数组
        inDegree = [0]*(numEdges+1)
        for i in range(numEdges):
            inDegree[edges[i][1]] += 1 
        # 步骤2，处理入度位2的边，看是否不构成环
        for i in range(numEdges-1,-1,-1):
            if inDegree[edges[i][1]] == 2:
                if not self.judgeCircle(edges,numEdges,i):
                    return edges[i]
        # 步骤3，处理入度为1的边，看是否不构成环
        for i in range(numEdges-1,-1,-1):
            if inDegree[edges[i][1]] == 1:
                if not self.judgeCircle(edges,numEdges,i):
                    return edges[i]
        
        raise ValueError("输入不符合要求")
    
    def judgeCircle(self,edges,numEdges,removeEdgeIndex):
        uf = UnionFind(numEdges + 1)
        for i in range(numEdges):
            if i == removeEdgeIndex:
                continue
            if not uf.union(edges[i][0],edges[i][1]):
                # 合并失败，说明edges[i][0],edges[i][1]在一个连通分量里，即构成环
                return True
        return False
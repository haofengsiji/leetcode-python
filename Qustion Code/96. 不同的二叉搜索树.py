# method_1
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                G[i] += G[j-1]*G[i-j]
        
        return G[-1]

# method_2
class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0]*(n+1)
        memo[0] = 1
        memo[1] = 1

        def dfs(root: int) -> int:
            if memo[root] != 0: return memo[root]

            for i in range(1,root+1):
                memo[root] += dfs(i - 1)*dfs(root - i)
            
            return memo[root]

        return dfs(n)

# method_3
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(1,n+1):
            C = (4*i-2)/(i+1)*C
        return int(C)
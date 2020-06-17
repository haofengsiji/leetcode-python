from typing import List
from collections import defaultdict 
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        path = defaultdict(list)
        for pair in relation:
            path[pair[1]].append(pair[0])
    
        def dfs(k,cur):
            if k == 1:
                if cur == 0:
                    return 1
                else:
                    return 0
            else:
                cnt = 0
                for i in path[cur]:
                    cnt += dfs(k-1,i)
            return cnt

        return dfs(k+1,n-1)

                    

if __name__ == "__main__":
    s = Solution()
    print(s.numWays(5,[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]],3))

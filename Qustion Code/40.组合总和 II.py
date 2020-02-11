class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def DFS(candidates,target,start,path):
            # 归
            if target == 0:
                ans.append(path.copy())
            
            # 递
            for i in range(start,len(candidates)):
                res = target - candidates[i]

                # 大剪枝
                if res < 0:
                    break
                
                # 小剪枝 -[1,2,5] [1,2,5]
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                    
                path.append(candidates[i])
                DFS(candidates,res,i+1,path)
                path.pop()
        
        candidates.sort()
        DFS(candidates,target,0,[])
        return ans

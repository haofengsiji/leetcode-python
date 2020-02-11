class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        # 存储变量
        path = []
        ans = []
        self.__dfs(candidates, ans, path, 0, target)

        return ans

    def __dfs(self, candidates, ans, path, start, target):
        
        # 归
        if target == 0:
            ans.append(path.copy())

        # 递
        for i in range(start,len(candidates)):
            res = target - candidates[i]

            # 剪枝
            if res < 0:
                continue
            
            path.append(candidates[i])
            self.__dfs(candidates, ans, path, i, res)
            path.pop()
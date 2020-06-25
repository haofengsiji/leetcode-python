# method_1
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = [None]*len(s)

        # 以索引i为起始到末尾的字符串能否由字典组成
        def dfs(i):
            # 长度超过s,返回True(空字符能组成)
            if i >= len(s): 
                return True
            # 存在以i为起始的递归结果
            if memo[i] != None:
                return memo[i]
            # 递归
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict and dfs(j+1):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)

# method_2
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        visited = [False]*len(s)
        q = collections.deque()
        q.append(0)

        while q:
            i = q.popleft()
            # 节点若访问则跳过
            if visited[i]: 
                continue
            else:
                visited[i] = True
            # 扫描从索引i开始的字符串
            for j in range(i,len(s)):
                # 子字符串在字典中
                if s[i:j+1] in wordDict:
                    # 并且到达结尾，返回True
                    if j == len(s) - 1:
                        return True
                    # 未到达结尾，则添加j+1起始索引到队列
                    else:
                        q.append(j+1)
        
        return False

# method_3
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # 前n个字符是否能由字典组成
        dp = [False]*(len(s)+1)
        
        # 初始状态
        dp[0] = True

        for i in range(1,len(s)+1): 
            for j in range(i,-1,-1):
                # 转移公式
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]
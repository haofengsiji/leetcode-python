# method_1 (从上到下)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 初始化
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        # 动态规划
        for i in range(1,n): # 每一行
            # 左边界
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            # 中间,常规情况
            for j in range(1,i):
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]
            # 右边界
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        
        return min(dp[-1])

# method_1.1 (从下到上)
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        // dp[i][j] 表示从点 (i, j) 到底边的最小路径和。
        int[][] dp = new int[n + 1][n + 1];
        // 从三角形的最后一行开始递推。
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = Math.min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle.get(i).get(j);
            }
        }
        return dp[0][0];
    }
}

作者：sweetiee
链接：https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-dp-bi-xu-miao-dong-by-sweetiee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# method_2
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 初始化
        n = len(triangle)
        dp = [0]*n
        dp[0] = triangle[0][0]

        # 动态规划（从右往左）
        for i in range(1,n): # 每一行
            # 右边界
            dp[i] = dp[i-1] + triangle[i][i]
            # 中间,常规情况
            for j in range(i-1,0,-1):
                dp[j] = min(dp[j],dp[j-1]) + triangle[i][j]
            # 左边界
            dp[0] = dp[0] + triangle[i][0]
        
        return min(dp)

# method_3
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        memo = []
        for i in range(m):
            memo.append([None]*(i+1))
        def dfs(i,j):
            if memo[i][j]:
                return memo[i][j]
            if i == m-1:
                res = triangle[i][j]
            else:
                res = triangle[i][j] + min(dfs(i+1,j),dfs(i+1,j+1))

            memo[i][j] = res
            return memo[i][j]

        return dfs(0,0)
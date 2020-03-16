class Solution:
    def coinChange(self, coins, amount: int) -> int:
        self.ans = float('inf')
        coins.sort(reverse=True)
        self.dfs(coins,0,amount,0)
        return self.ans if self.ans != float('inf') else -1

    def dfs(self,coins,c_index,amount,cnt):
        if c_index == len(coins) or cnt > self.ans:
            return
        elif amount == 0:
            self.ans = min(self.ans,cnt)
            return
        k = amount//coins[c_index]
        while k >= 0:
            self.dfs(coins,c_index+1,amount-k*coins[c_index],cnt+k)
            k -= 1


 

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1,2,5],11))


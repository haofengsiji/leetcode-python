from typing import List
from collections import defaultdict 
import sys

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.anss = []
        self.dfs(s,'','',0)
        return self.anss

    def dfs(self,res_s,ans,cur,cnt):
        # 满足规则
        if cnt >= 4:
            return
        if cur != '' and int(cur)>255:
            return
        
        # 符合条件的返回
        if res_s == '':
            if cnt == 3:
                if cur == '0' or cur[0] != '0':
                    ans = ans + '.' + cur
                    self.anss.append(ans[1:])
            return
        
        # 分割
        if cur != '':
            if cur == '0' or cur[0] != '0':
                self.dfs(res_s, ans + '.' + cur, '', cnt + 1)
            

            
        # 不分割
        self.dfs(res_s[1:],ans, cur + res_s[0], cnt)
        return

if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("010010"))

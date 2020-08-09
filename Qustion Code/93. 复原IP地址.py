# method_1.1

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        SEG_COUNT = 4
        ans = list()
        segments = [0] * SEG_COUNT
        
        def dfs(segId: int, segStart: int):
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
            if segId == SEG_COUNT:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return
            
            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
            if segStart == len(s):
                return

            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
            if s[segStart] == "0":
                segments[segId] = 0
                dfs(segId + 1, segStart + 1)
            
            # 一般情况，枚举每一种可能性并递归
            addr = 0
            for segEnd in range(segStart, len(s)):
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break


        dfs(0, 0)
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/restore-ip-addresses/solution/fu-yuan-ipdi-zhi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# method_1.2
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
    
# method_2
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        l=len(s)
        if l>12 or l<4: return []
        arr=[]
        # 遍历三个间隔位置
        for i in range(1,min(4,l-2)):
            for j in range(i+1,min(i+4,l-1)):
                for k in range(j+1,min(j+4,l)):
                    if l-k>3: continue
                    n=[s[:i],s[i:j],s[j:k],s[k:]]
                    flag=False
                    for c in n: 
                        if c[0]=='0' and c!='0': 
                            flag=True
                            break
                    if flag: continue
                    # print(n)
                    a,b,c,d=map(int,n)
                    if 0<=a<=255 and 0<=b<=255 and 0<=c<=255 and 0<=d<=255:
                        arr.append(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
        return arr
class Trie:
    def __init__(self):
        self.next = [None]*26
        self.isEnd = False
    
    def insert(self,s:str):
        curPos = self

        for c in s[::-1]:
            t = ord(c) - 97
            if curPos.next[t] == None:
                curPos.next[t] = Trie()
            curPos = curPos.next[t]
        curPos.isEnd = True


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        root = Trie()
        for word in dictionary:
            root.insert(word)
        
        dp = [n+1]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = dp[i-1] + 1

            curPos = root
            for j in range(i,0,-1):
                t = ord(sentence[j-1]) - 97
                if curPos.next[t] == None:
                    break
                elif curPos.next[t].isEnd:
                    dp[i] = min(dp[i],dp[j-1])
                if dp[i] == 0:
                    break
                curPos = curPos.next[t]
        return dp[-1]
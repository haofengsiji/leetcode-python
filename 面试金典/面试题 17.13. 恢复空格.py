# metbod_1
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dp = [n+1]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = dp[i-1] + 1
            for j in range(i, 0, -1):
                if sentence[j-1:i] in dictionary:
                    dp[i] = min(dp[i], dp[j-1])
        return dp[-1]

# method_2
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

# method_3
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        base = 41
        mod = 1<<31-1
        n = len(sentence)
    
        def getHash(s:str):
            hashValue = 0
            for c in s[::-1]:
                hashValue = hashValue * base + ord(c) - 97 + 1
                hashValue = hashValue % mod
            
            return hashValue
        
        hashValues = set()
        for word in dictionary:
            hashValues.add(getHash(word))
        
        dp = [n+1]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = dp[i-1] + 1
            hashValue = 0
            for j in range(i,0,-1):
                t = ord(sentence[j-1]) - 97 + 1
                hashValue = hashValue * base + t
                hashValue = hashValue % mod
                if hashValue in hashValues:
                    dp[i] = min(dp[i],dp[j-1])

        return dp[-1]   




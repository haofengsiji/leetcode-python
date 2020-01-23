class Solution:
    def findSubstring(self, s: str, words):
        n = len(s)
        l_word = len(words[0])
        length = len(words)*l_word
        flag = True
        out = []
        # 哈希表1
        hash1 = {}
        hash2 = {}
        for word in words:
            hash1.setdefault(word, 0)
            hash1[word] += 1
        for i in range(0,n-length+1):
            # 构建哈希表2
            for j in range(i,i+length,l_word):
                hash2.setdefault(s[j:j+l_word], 0)
                hash2[s[j:j+l_word]] += 1
            # 判断
            for key in hash2:
                if key in hash1 and hash1[key] == hash2[key]:
                    continue
                else:
                    flag = False
                    break
                    
            if flag == True:
                out.append(i)
            else:
                flag == True
            hash2 = {}

        return out 
                    

if __name__ == "__main__":
    s = Solution()

    print(s.findSubstring("barfoothefoobarman",["foo","bar"]))
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == "" or words == []: return []
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
            if hash1 == hash2:
                 out.append(i)
            hash2 = {}

        return out 

# method_2
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not words or not s: return []
        num_words = len(words)
        word_len = len(words[0])
        words_counter = Counter(words)
        n = len(s)
        ans = []
        
        for i in range(word_len):
            right = i
            left = i
            cur_conter = Counter()
            cur_num = 0
            while right + word_len <= n:
                w = s[right:right+word_len]
                cur_conter[w] += 1
                cur_num += 1
                right += word_len
                while cur_conter[w] > words_counter[w]:
                    left_w = s[left:left+word_len]
                    cur_conter[left_w] -= 1
                    cur_num -=1
                    left += word_len
                if cur_num == num_words:
                    ans.append(left)
        return ans 
                    
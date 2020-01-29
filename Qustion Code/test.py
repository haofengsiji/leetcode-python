class Solution:
    def findSubstring(self, s: str, words):
        from collections import Counter
        if words == []: return []
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


        
                    

if __name__ == "__main__":
    s = Solution()

    print(s.findSubstring("aaa",["a","a"]))
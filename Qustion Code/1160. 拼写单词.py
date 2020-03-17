# method_1
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = {}
        ans = 0

        for c in chars:
            char_map[c] = char_map.get(c, 0) + 1
        
        for word in words:
            flag = 1
            for j in word:
                if word.count(j) > char_map.get(j, 0):
                    flag = 0
                    break
            if flag == 0:
                continue
            else:
                ans += len(word)
        return ans

# 其他写法
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cnt = collections.Counter(chars)
        for w in words:
            c = collections.Counter(w)
            if all([c[i] <= cnt[i] for i in c]):
                ans += len(w)
        return ans

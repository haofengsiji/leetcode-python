from typing import List
from collections import defaultdict 
import sys

class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j = 0,0
        for read,c in enumerate(chars):
            if read+1 == len(chars) or chars[read+1] != c:
                chars[j] = chars[i]
                j += 1
                if read > i:
                    digits = str(read - i + 1)
                    for digit in digits:
                        chars[j] = digit
                        j += 1
                i = read + 1
        return i
                
                    

if __name__ == "__main__":
    chars = ["a","a","a","b","b","a","a"]
    s = Solution()
    s.compress(chars)
    print(chars)

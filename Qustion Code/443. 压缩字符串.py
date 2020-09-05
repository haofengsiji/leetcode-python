class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor,write = 0,0
        for read,c in enumerate(chars):
            if read+1 == len(chars) or chars[read+1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    digits = str(read - anchor + 1)
                    for digit in digits:
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write

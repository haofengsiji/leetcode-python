class Solution:
    def test(self, n):
        ans = '1'
        for c in range(1,n):
            temp = ''
            i = 0
            j = 0
            while j < len(ans):
                if ans[i] == ans[j]:
                    j +=1
                else:
                    temp += str(j-i) + ans[i]
                    i = j
                    j += 1    
            temp += str(j-i) + ans[i]
            ans = temp
        return ans


 

if __name__ == "__main__":
    s = Solution()
    print(s.test(5))


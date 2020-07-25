# method_1
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

# method_2
class Solution:
    def divisorGame(self, N: int) -> bool:
        f = [False]*(N+2)
        f[2] = True

        for i in range(3,N+1):
            for j in range(1,i):
                if i % j == 0 and f[i-j] == False:
                    f[i] = True
                    break
        
        return f[N]
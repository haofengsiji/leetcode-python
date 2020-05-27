# method_1
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = 0
        hashmp = {0:1}
        cnt = 0
        for a in A:
            prefix += a
            rmd = prefix % K
            same = hashmp.get(rmd,0)
            cnt += same
            hashmp[rmd] = same + 1
        return cnt
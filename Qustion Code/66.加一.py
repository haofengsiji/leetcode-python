# method_1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        ans_digits  = []
        for d in digits:
            ans = ans*10 + d
        ans = ans +1
        while ans != 0:
            temp = ans%10
            ans = ans//10
            ans_digits.append(temp)
        return ans_digits[::-1]

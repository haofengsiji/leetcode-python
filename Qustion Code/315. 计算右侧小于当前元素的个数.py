# method_1
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0]*n
        for i in range(n):
            for j in range(i+1,n):
                if nums[j] < nums[i]:
                    counts[i] += 1
        return counts

# method_2
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        a = nums.copy().sort()
        c = [0]*len(nums)
        ret = [0]*len(nums)

        def LowBit(x:int)->int:
            return x&(-x)
        
        def Update(n:int, pos:int):
            while (pos < n):
                c[pos] += 1
                pos += LowBit(pos)
        
        def Query(pos:int)->int:
            ret = 0

            while pos > 0:
                ret += c[pos]
                pos -= LowBit(pos)
            
            return ret

        def lower_bound(n:int, x:int)->int:
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high)//2
                if a[mid] < x:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        
        def Discretization(n:int) -> int:
            m = 0
            for i in range(n):
                if a[i] > a[m]:
                    a[m] = a[i]
                    m += 1
            return m + 1
        
        m = Discretization(len(nums))
        for i in range(len(nums)-1,-1,-1):
            idx = lower_bound(m,nums[i]) + 1
            ret[idx] = Query(idx-1)
            Update(m,idx)
        
        return ret

       
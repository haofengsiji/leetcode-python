n = int(input())
nums = list(map(int,input().split(' ')))

def DivideAndConquer(left,right):
    # 归
    if left == right:
        return nums[left]
    # 递
    mid = (left + right)//2
    maxLeft = DivideAndConquer(left,mid)
    maxRight = DivideAndConquer(mid+1,right)
    # 合
    maxLeftBorderSum = 0
    leftBorderSum = 0
    for i in range(mid,left-1,-1):
        leftBorderSum += nums[i]
        maxLeftBorderSum = max(leftBorderSum,maxLeftBorderSum)
    maxRightBorderSum = 0
    rightBorderSum = 0
    for i in range(mid+1,right+1):
        rightBorderSum += nums[i]
        maxRightBorderSum = max(rightBorderSum,maxRightBorderSum)
    return max(maxLeft,maxRight,maxLeftBorderSum + maxRightBorderSum)

print(DivideAndConquer(0,n-1)) 
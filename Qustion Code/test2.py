n = int(input())
nums = list(map(int,input().split(' ')))
prefix = 0
ans = 0
ans_s = 0
ans_e = n - 1
zero = n
s = 0
e = -1

for i,num in enumerate(nums):
    prefix += num
    e = i
    if prefix < 0:
        prefix = 0
        s = i + 1
    else:
        if prefix > ans:
            ans = prefix
            ans_s = s
            ans_e = e
        elif prefix == ans:
            zero = min(zero,i)

if ans == 0 and zero != -1:
    print(0,0,0)
else:
    print(ans,nums[ans_s],nums[ans_e])
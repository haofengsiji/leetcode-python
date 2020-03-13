# method_1
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        cand_list = [0 for _ in range(num_people)]
        # 初始化
        cur_cand = 1
        cur_child = 0
        while candies > 0:
            if cur_child == num_people:
                cur_child = 0
            # 不够发了
            if candies < cur_cand:
                cand_list[cur_child] += candies
                candies = 0
            # 按规则发放
            else:
                cand_list[cur_child] += cur_cand
                candies -= cur_cand
                cur_cand += 1
            cur_child += 1
        return cand_list

# method_1 官解，简洁版，
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0]*num_people
        i = 0
        while candies > 0:
            ans[i % num_people] += min(i+1,candies)
            candies -= min(i+1,candies)
            i += 1
        return ans

# method_2 数学法
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0]*num_people
        # 获得完整礼物的人数 p
        p = int((2*candies + 0.25)**0.5 - 0.5)
        # 完整部分分发
        rows = p // num_people
        cols = p % num_people
        for i in range(num_people):
            ans[i] = (i+1)*rows + int(num_people*rows*(rows-1)/2)
            # 不完整部分分发
            if i < cols:
                ans[i] += (i+1) + num_people*rows
        # 剩余分发
        ans[cols] += candies - int(p*(p + 1)/2)
        
        return ans
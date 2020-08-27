# method_1
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)
        
        vec = collections.defaultdict(list)
        for depart,arrive in tickets:
            vec[depart].append(arrive)
        for key in vec.keys():
            heapq.heapify(vec[key])
        stack = []
        dfs("JFK")
        return stack[::-1]
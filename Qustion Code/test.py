import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态: 0=未搜索 1=搜索中 2=搜索完成
        visited = [0] * numCourses
        # 列表模拟栈，下标0为栈底，n-1为栈顶
        result = list()
        # 判断图中是否有环
        invalid  = False

        # 构建图
        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal invalid 
            # 将节点标记为搜索中
            visited[u] = 1
            # 搜索相邻节点
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if invalid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    invalid = True
            # 节点u[搜索完成]
            visited[u] = 2
            # 将节点u入栈
            result.append(u)
        
        # 每次挑选一个[未搜索]的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if not invalid and visited[i] == 0:
                dfs(i)
        
        # 有环，没有答案
        if invalid:
            return list()

        # 如果无环，返回栈
        # 注意下标 0 为栈底，因此需要将数组反序输出
        return result[::-1]


 

if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(2,[[0,1]]))


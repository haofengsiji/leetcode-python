# method_1
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNVISITED, RED, BLUE = 0, -1, 1 # Color flag
        color = [UNVISITED]*n
        valid = True

        def dfs(node:int,c:int):
            nonlocal valid
            color[node] = c
            # Traverse node's neighbors
            for nbr in graph[node]:
                if color[nbr] == c: # same color as node
                    valid = False
                    return
                elif color[nbr] == 0: # unvisited nbr
                    dfs(nbr,-c)
                else: # visited nbr
                    continue
            return
        
        # Traverse all nodes
        for i in range(n):
            if color[i] != 0:
                continue
            dfs(i,RED)
            if not valid:
                break
        
        return valid

# method_2
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNVISITED, RED, BLUE = 0, -1, 1 # color flags
        color = [UNVISITED]*n
        # Traverse all nodes
        for i in range(n):
            if color[i] != UNVISITED:
                continue
            q = collections.deque([i])
            color[i] = RED
            while q:
                node = q.popleft()
                cNbr = -color[node]
                for nbr in graph[node]:
                    if color[nbr] == UNVISITED:
                        color[nbr] = cNbr
                        q.append(nbr)
                    elif color[nbr] == -cNbr:
                        return False
                    else:
                        continue

        return True 
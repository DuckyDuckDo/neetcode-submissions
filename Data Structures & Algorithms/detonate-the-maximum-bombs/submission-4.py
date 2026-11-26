from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def calculate_distance(x1, y1, x2, y2):
            return abs(((x2-x1)**2 + (y2 - y1) **2) ** 0.5)
        
        graph = {}
        for i, (x1, y1, r1) in enumerate(bombs):
            graph[i] = []
            for j, (x2, y2, r2) in enumerate(bombs):
                if i == j:
                    continue
                distance = calculate_distance(x1,y1,x2,y2)
                if distance <= r1:
                    graph[i].append(j)
        

        def bfs(start_bomb, graph):
            queue = deque([start_bomb])
            bomb_count = 0
            visited = set([start_bomb])
            while queue:
                curr_bomb = queue.popleft()
                bomb_count += 1
                for neighbor_bomb in graph[curr_bomb]:
                    if neighbor_bomb not in visited:
                        visited.add(neighbor_bomb)
                        queue.append(neighbor_bomb)

            return bomb_count


        res = 0 
        for i in range(len(bombs)):
            res = max(res, bfs(i, graph))
        return res
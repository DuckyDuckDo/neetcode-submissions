class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        sys.setrecursionlimit(20000)

        n = len(graph)

        safe = {} # Holds the safe states we have found thus far
        def dfs(i):
            if i in safe:
                return safe[i]
            
            safe[i] = False # Assume false because if we reach it again, it will be a cycle which is guaranteed to be false
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False
            safe[i] = True
            return safe[i]

        return [i for i in range(n) if dfs(i)]
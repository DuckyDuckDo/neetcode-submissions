class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # We are to find all nodes that are not part of cycles or if it reaches a cycle
        outdegree = [len(node) for node in graph]

        #outdegree ->  [1, 1, 0]
        incoming_nodes = [[] for _ in graph]

        for source, row in enumerate(graph):
            for destination in row:
                incoming_nodes[destination].append(source)


        queue = [i for i, x in enumerate(outdegree) if x == 0]

        for node in queue:
            for prev_node in incoming_nodes[node]:
                outdegree[prev_node] -= 1
                if outdegree[prev_node] == 0:
                    queue.append(prev_node)


        return [i for i, x in enumerate(outdegree) if x == 0]
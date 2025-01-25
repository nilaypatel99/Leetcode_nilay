class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        # Step 1: Reverse the graph
        reverse_graph = [[] for _ in range(n)]
        outdegree = [0] * n
        
        for node in range(n):
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)
            outdegree[node] = len(graph[node])
        
        # Step 2: Collect terminal nodes (with zero outdegree)
        queue = deque()
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
        
        # Step 3: Process nodes with zero outdegree
        safe_nodes = set()
        while queue:
            node = queue.popleft()
            safe_nodes.add(node)
            
            for neighbor in reverse_graph[node]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Return the sorted list of safe nodes
        return sorted(safe_nodes)

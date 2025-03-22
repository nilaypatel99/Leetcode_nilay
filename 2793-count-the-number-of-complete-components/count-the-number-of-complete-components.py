from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Step 1: Build adjacency list representation of the graph
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        complete_components = 0
        
        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    component.add(curr)
                    stack.extend(graph[curr] - visited)  # Visit unvisited neighbors
        
        # Step 2: Find connected components and check for completeness
        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node, component)
                
                # Step 3: Check if the component forms a complete graph
                size = len(component)
                edge_count = sum(len(graph[v]) for v in component) // 2  # Each edge counted twice
                if edge_count == (size * (size - 1)) // 2:
                    complete_components += 1
        
        return complete_components

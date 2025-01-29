class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Helper function to find the root parent with path compression
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        # Helper function to union two sets
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parent[root1] = root2  # Union by rank can be added for optimization

        # Initialize each node's parent to itself
        parent = list(range(len(edges) + 1))

        # Process each edge
        for a, b in edges:
            if find(a) == find(b):  # Cycle detected
                return [a, b]
            else:
                union(a, b)



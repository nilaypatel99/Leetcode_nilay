class Solution:
    def isBipartite(self, adj, curr, colors, currColor):
        colors[curr] = currColor
        for ngbr in adj[curr]:
            if colors[ngbr] == colors[curr]:
                return False
            if colors[ngbr] == -1:
                if not self.isBipartite(adj, ngbr, colors, 1 - currColor):
                    return False
        return True
    
    def bfs(self, adj, currNode, n):
        que = deque([currNode])
        visited = [False] * n
        visited[currNode] = True
        level = 1
        
        while que:
            size = len(que)
            for _ in range(size):
                curr = que.popleft()
                for ngbr in adj[curr]:
                    if not visited[ngbr]:
                        que.append(ngbr)
                        visited[ngbr] = True
            level += 1
        
        return level - 1
    
    def getMaxFromEachComp(self, adj, curr, visited, levels):
        maxGrp = levels[curr]
        visited[curr] = True
        for ngbr in adj[curr]:
            if not visited[ngbr]:
                maxGrp = max(maxGrp, self.getMaxFromEachComp(adj, ngbr, visited, levels))
        return maxGrp
    
    def magnificentSets(self, n, edges):
        adj = defaultdict(list)
        for edge in edges:
            u = edge[0] - 1  # converting to 0-based index
            v = edge[1] - 1
            adj[u].append(v)
            adj[v].append(u)

        # Bipartite check
        colors = [-1] * n
        for node in range(n):
            if colors[node] == -1:
                if not self.isBipartite(adj, node, colors, 1):
                    return -1

        # BFS to find max levels for each node
        levels = [0] * n
        for node in range(n):
            levels[node] = self.bfs(adj, node, n)

        # Get max groups for each component
        maxGroupEachComp = 0
        visited = [False] * n
        for node in range(n):
            if not visited[node]:
                maxGroupEachComp += self.getMaxFromEachComp(adj, node, visited, levels)

        return maxGroupEachComp

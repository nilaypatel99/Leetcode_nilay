class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
            n = len(favorite)
            adj = defaultdict(list)

            # Reverse the graph to facilitate finding path lengths
            for u in range(n):
                v = favorite[u]
                adj[v].append(u)

            longest_cycle_count = 0
            happy_couple_count = 0
            visited = [False] * n

            for i in range(n):
                if not visited[i]:
                    node_to_index = {}
                    curr_node = i
                    curr_node_count = 0

                    while not visited[curr_node]:
                        visited[curr_node] = True
                        node_to_index[curr_node] = curr_node_count

                        next_node = favorite[curr_node]
                        curr_node_count += 1

                        if next_node in node_to_index:  # Cycle detected
                            cycle_length = curr_node_count - node_to_index[next_node]
                            longest_cycle_count = max(longest_cycle_count, cycle_length)

                            if cycle_length == 2:  # Happy couple case (cycle of length 2)
                                visited_nodes = [False] * n
                                visited_nodes[curr_node] = True
                                visited_nodes[next_node] = True
                                happy_couple_count += (
                                    2
                                    + self.BFS(curr_node, adj, visited_nodes)
                                    + self.BFS(next_node, adj, visited_nodes)
                                )
                            break

                        curr_node = next_node

            return max(happy_couple_count, longest_cycle_count)

    def BFS(self, start, adj, visited):
            """
            Perform BFS to calculate the longest chain starting from 'start'.
            """
            queue = deque([(start, 0)])  # (node, path length)
            max_distance = 0

            while queue:
                curr_node, dist = queue.popleft()

                for neighbor in adj[curr_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, dist + 1))
                        max_distance = max(max_distance, dist + 1)

            return max_distance

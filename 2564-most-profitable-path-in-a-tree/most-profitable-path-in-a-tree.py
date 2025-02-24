from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Step 1: Build the tree as an adjacency list
        n = len(amount)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Find Bob's arrival times to each node
        bob_time = [-1] * n  # -1 means Bob never visits this node
        
        def dfs_bob(node: int, parent: int, time: int) -> bool:
            """DFS to record Bob's arrival time at each node."""
            bob_time[node] = time
            if node == 0:  # Bob has reached the root
                return True
            for neighbor in graph[node]:
                if neighbor != parent:
                    if dfs_bob(neighbor, node, time + 1):
                        return True
            bob_time[node] = -1  # Backtrack if node 0 is not in this path
            return False
        
        dfs_bob(bob, -1, 0)

        # Step 3: DFS for Alice to maximize profit
        max_profit = float('-inf')

        def dfs_alice(node: int, parent: int, time: int, income: int):
            nonlocal max_profit
            # Determine income at this node
            if bob_time[node] == -1 or time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2  # Share the amount
            # Else, Bob already passed, Alice gets nothing at this node

            # Check if it's a leaf node
            is_leaf = True
            for neighbor in graph[node]:
                if neighbor != parent:
                    is_leaf = False
                    dfs_alice(neighbor, node, time + 1, income)

            if is_leaf:
                max_profit = max(max_profit, income)

        dfs_alice(0, -1, 0, 0)

        return max_profit

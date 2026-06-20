class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # 1. Add the implicit restriction for building 1 and sort
        restrictions.append([1, 0])
        restrictions.sort()
        
        m = len(restrictions)
        
        # 2. Left-to-Right Pass
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + dist)
            
        # 3. Right-to-Left Pass
        for i in range(m - 2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + dist)
            
        # 4. Find the maximum height achieved anywhere
        max_height = 0
        
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            
            # Peak height achievable between id1 and id2
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
            
        # 5. Handle the open-ended space after the last restricted building up to n
        last_id, last_h = restrictions[-1]
        max_height = max(max_height, last_h + (n - last_id))
        
        return max_height
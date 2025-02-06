class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
     
        product_map = defaultdict(list)
        n = len(nums)
        
        # Store product pairs in a hash map
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product].append((nums[i], nums[j]))

        # Count valid tuples
        count = 0
        for pairs in product_map.values():
            k = len(pairs)
            if k > 1:
                count += (k * (k - 1) // 2) * 8  # Compute combinations and multiply by 8

        return count

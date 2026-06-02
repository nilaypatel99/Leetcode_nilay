class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        res = 0

        for i in range(len(cost)):
            if i % 3 != 2:  # pay for first two candies in each group of 3
                res += cost[i]

        return res
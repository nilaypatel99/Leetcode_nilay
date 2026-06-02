class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish=float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_end=max(landStartTime[i],0)+landDuration[i]
                finish1=max(land_end,waterStartTime[j])+waterDuration[j]

                water_end=max(waterStartTime[j],0)+waterDuration[j]
                finish2=max(water_end,landStartTime[i])+landDuration[i]

                min_finish=min(min_finish,finish1,finish2)
                
        return min_finish


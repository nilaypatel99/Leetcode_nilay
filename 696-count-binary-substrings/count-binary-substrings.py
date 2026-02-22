class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 0-0-1-1-->0011,01
        # 0-1-->not consecutive
        # 1-1-0-0-->1100,10
        # 1-0-->not consecutive
        # 0-0-1-1-->0011,01
        #can be completed in O(n) if the pattern is +1 like in the 0011,1100 it will always have 1 even if number of zeros are more 

        prev_len=0
        cur_len=1
        ans=0

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cur_len+=1
            else:
                ans+=min(prev_len,cur_len)
                prev_len=cur_len
                cur_len=1
        ans += min(prev_len, cur_len)
        return ans

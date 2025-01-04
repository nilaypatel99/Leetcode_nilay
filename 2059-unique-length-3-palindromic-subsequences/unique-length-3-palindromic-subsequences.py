class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurence=[float('inf')]*26
        last_occurence=[0]*26
        res=0
        
        # first and last occurrence of each character
        for i,ch in enumerate(s):
            idx=ord(ch)-ord('a')
            first_occurence[idx]=min(first_occurence[idx],i)
            last_occurence[idx]=i
        
        #number of unique char between the first and last char
        for i in range(26):
            if first_occurence[i]<last_occurence[i]:
                unique_char=set(s[first_occurence[i]+1 : last_occurence[i]])       
                res+=len(unique_char)
        return res

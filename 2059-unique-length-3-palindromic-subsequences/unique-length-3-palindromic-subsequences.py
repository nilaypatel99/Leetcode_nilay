class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #Brute Force: we can use three for loops to get the unique palindrome 
        #optimized: iterate through the each char and make a left and right sect and check if the char in left is 
        #present in right,we use map for right and set for left to store the two halfs
        #better optimized: we can add the current char to left and remove the char found in right

        res=set()  #to store unique palindrome just the left and right
        left=set()
        right=Counter(s)

        for m in s:     #check the current
            right[m]-=1    #remove from right
            
            for char in left:
                if right[char]>0:
                    res.add((char,m))
            left.add(m)
        return len(res)



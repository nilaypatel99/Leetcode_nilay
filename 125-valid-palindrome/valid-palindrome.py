class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=''.join(char for char in s if char.isalnum()).lower()
        left,right=0,len(temp)-1
        while left<right:
            if temp[left]==temp[right]:
                left+=1
                right-=1
            else:
                return False
        return True
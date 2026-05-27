class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #store the first occurence of upper case and last occurence of lower case
        #and store the index of both the uppercase and lower case 
        #and if index of lower case is greater than upper case ignore it
        #else update the count of it

        lower={}
        upper={}
        cnt=0

        for idx,ele in enumerate(word):
            if ele.islower():
                lower[ele]=idx
            else:
                c=ele.lower()
                if c not in upper:
                    upper[c]=idx
        
        for c in lower:
            if c in upper and lower[c]<upper[c]:
                cnt+=1
        
        return cnt

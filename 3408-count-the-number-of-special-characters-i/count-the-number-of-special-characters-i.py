class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        sp_cnt=0
        res=set(word)

        print(res)

        for char in res:
            if char.islower() and char.upper() in res:
                sp_cnt+=1
            else:
                continue
        return sp_cnt

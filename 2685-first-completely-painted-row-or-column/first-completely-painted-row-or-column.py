class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows=len(mat)
        cols=len(mat[0])

        chk={}
        for r in range(rows):
            for c in range(cols):
                chk[mat[r][c]]=(r,c)
        
        row_cnt=[0]*rows
        col_cnt=[0]*cols

        for i,val in enumerate(arr):
            r,c=chk[val]

            if mat[r][c]!='#':
                mat[r][c]='#'

                row_cnt[r]+=1
                col_cnt[c]+=1

                if row_cnt[r]==cols:
                    return i
                if col_cnt[c]==rows:
                    return i
        return -1
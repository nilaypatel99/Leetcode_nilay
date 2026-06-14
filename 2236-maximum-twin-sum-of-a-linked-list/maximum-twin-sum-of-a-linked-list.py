# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals=[]

        while head:
            vals.append(head.val)
            head=head.next

        l,r=0,len(vals)-1
        res=float('-inf')

        while l<r:
            res=max(res,vals[l]+vals[r])
            l+=1
            r-=1
        return res
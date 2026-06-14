# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr=slow

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        first=head
        second=prev
        res=0

        while second:
            res=max(res,first.val+second.val)
            first=first.next
            second=second.next
        return res
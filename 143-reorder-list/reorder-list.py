# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        right=slow.next
        slow.next=None
        prev=None
        while right:
            tmp=right.next
            right.next=prev
            prev=right
            right=tmp
        second=prev
        first=curr
        while first and second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2




        """
        Do not return anything, modify head in-place instead.
        """
        

# left_l: 1 ->2
# right_l: 3->4 (4->3)
# merge:
# 1->2 and 4->3

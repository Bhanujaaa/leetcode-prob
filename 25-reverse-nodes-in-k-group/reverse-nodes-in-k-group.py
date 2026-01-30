# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grouprev=dummy
        while True:
            kth=self.remove(grouprev,k)
            if kth is None:
                break
            groupnext=kth.next
            curr=grouprev.next
            prev=kth.next
            while curr!=groupnext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            tmp1=grouprev.next
            grouprev.next=kth
            grouprev=tmp1
        return dummy.next


    def remove(self,node,k):
        while node and k>0:
            node=node.next
            k-=1
        return node
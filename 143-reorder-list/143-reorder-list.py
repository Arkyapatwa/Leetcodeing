# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        cur=slow.next
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        slow.next=None
        list1=head
        list2=prev
        while list2:
            nex=list1.next
            list1.next=list2
            list1=list2
            list2=nex

        
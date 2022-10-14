# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size=0
        cur=head
        while cur:
            cur=cur.next
            size+=1
        if size==1:
            return 
        mid=head
        for _ in range((size//2)-1):
            mid=mid.next
        mid.next=mid.next.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         making reverse of the first list
        prev=None
        cur=l1
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        l1=prev
#         making reverse of the second list
        prev=None
        cur=l2
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        l2=prev
#         newlist to store values
        newlist=ListNode(0)
        res=newlist
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            newlist.next=ListNode(carry%10)
            newlist=newlist.next
            carry//=10
        
        prev=None
        cur=res.next
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        res=prev
               
        return res
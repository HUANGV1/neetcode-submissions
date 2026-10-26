# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # if n=2, to check if current node is nth from the end, we need to see if n.next.next=None

        dummy=ListNode(0, head)

        fast=dummy

        for _ in range(n-1):
            fast=fast.next
        
        slow=dummy
        prev=None

        while fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next
        
        prev.next=slow.next

        return dummy.next

        
        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        [2,4,6,8,10]

        2,10,4,8,6

        find the middle, reverse the elements from the middle to the end, then alternate between adding starting from the front, middle

        [2,4,6,8,10]
        [2,4,10,8,6]

        2 10 4 8 6

        [2,4,6,10,8]
        2 10 4 8 6

        '''

        # find the middle

        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # slow is now the middle 

        second=slow.next
        slow.next=None

        # reverse the list from slow to the end. fast is right now the end

        prev=None
        curr=second

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        # now prev is the middle Node

        curr=head
        second=prev
        while second:
            next_curr=curr.next
            next_second=second.next

            curr.next=second
            second.next=next_curr

            curr=next_curr
            second=next_second
            

        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1==None: return list2
        if list2==None: return list1

        if list1.val<list2.val:
            dummy=list1
            list1_pointer=list1.next
            list2_pointer=list2
        else:
            dummy=list2
            list1_pointer=list1
            list2_pointer=list2.next

        head=dummy

        while list1_pointer and list2_pointer:
            if list1_pointer.val<list2_pointer.val:
                dummy.next=list1_pointer
                list1_pointer=list1_pointer.next
            else:
                dummy.next=list2_pointer
                list2_pointer=list2_pointer.next

            dummy=dummy.next
            
        if list1_pointer:
            dummy.next=list1_pointer
        else:
            dummy.next=list2_pointer
        
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ahead = ListNode()
        head = ListNode()
        ahead.next = head

        if list1 is None:
            return list2
        elif list2 is None :
            return list1
            
        while list1 is not None and list2 is not None :
            if list1.val > list2.val :
                node = ListNode(list2.val)
                head.next = node
                head = head.next
                list2 = list2.next
            elif list1.val <= list2.val :
                node = ListNode(list1.val)
                head.next = node
                head = head.next
                list1 = list1.next

            if list1 is None :
                head.next = list2
            elif list2 is None :
                head.next = list1

        return ahead.next.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        while head :
            head_list.append(head.val)
            head = head.next
        head_list.reverse()

        ahead = ListNode()
        reverse_haed = ListNode()
        ahead.next = reverse_haed
        
        for i, item in enumerate(head_list) :
            if i == 0 :
                reverse_haed.val = item
            else :
                node = ListNode(item)
                reverse_haed.next = node
                reverse_haed = reverse_haed.next

        if len(head_list) == 0 :
            return head
        return ahead.next




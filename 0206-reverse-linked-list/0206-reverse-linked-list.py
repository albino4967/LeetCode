# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        while head :
            head_list.append(ListNode(head.val))
            head = head.next
        head_list.reverse()

        print(head_list)

        for i, item in enumerate(head_list):
            if i+1 >= len(head_list) : break
            item.next = head_list[i+1]

        if len(head_list) == 0 :
            return head

        return head_list[0]



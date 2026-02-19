# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        re = k % count
        if re == 0:
            return head
        temp = head
        ind = count - re - 1
        while ind:
            ind -= 1
            temp = temp.next
        tn = temp.next
        temp.next = None
        temp = tn
        while temp.next:
            temp = temp.next
        temp.next = head
        return tn





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            # If duplicate sequence found
            if head.next and head.val == head.next.val:
                # Skip all nodes with same value
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next

        return dummy.next

    '''class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        h = t = None

        while head:
            
            # Case 1: Duplicate detected
            if head.next and head.val == head.next.val:
                dup = head.val
                
                # Skip entire duplicate group
                while head and head.val == dup:
                    head = head.next
            
            else:
                # Unique node → add to new list
                tm = head
                head = head.next
                tm.next = None
                
                if h is None:
                    h = t = tm
                else:
                    t.next = tm
                    t = tm

        return h
'''
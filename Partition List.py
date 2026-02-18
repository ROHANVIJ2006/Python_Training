# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create dummy heads for both partitions
        less_head = ListNode(0)
        greater_head = ListNode(0)

        # Pointers to the current end of each partition
        less = less_head
        greater = greater_head

        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        # Connect the partitions
        less.next = greater_head.next
        # End the greater partition
        greater.next = None

        return less_head.next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        H = None
        P = None

        while list1 and list2:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next

            temp.next = None

            if H == None:
                H = P = temp
            else:
                P.next = temp
                P = temp

        while list1:
            temp = list1
            list1 = list1.next
            temp.next = None
            if H == None:
                H = P = temp
            else:
                P.next = temp
                P = temp

        while list2:
            temp = list2
            list2 = list2.next
            temp.next = None
            if H == None:
                H = P = temp
            else:
                P.next = temp
                P = temp

        return H

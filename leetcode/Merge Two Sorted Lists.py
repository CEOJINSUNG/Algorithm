from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        array = []

        while list1 != None:
            array.append(list1.val)
            list1 = list1.next
        
        while list2 != None:
            array.append(list2.val)
            list2 = list2.next

        if len(array) == 0:
            return None

        array.sort(reverse = True)
        node = ListNode(val=array[0])
        for i in range(1, len(array)):
            num = array[i]
            head = ListNode(val=num, next=node)
            node = head
        return node
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        
        newNode = head
        while newNode != None:
            nums.append(newNode.val)
            newNode = newNode.next
        
        nums.sort()
        newNode, i = head, 0 
        while newNode:
            newNode.val = nums[i]  
            i += 1
            newNode = newNode.next
        
        return head

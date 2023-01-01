class Solution(object):
    def hasCycle(self, head):
        fastptr = head
        slowptr = head
        while fastptr is not None and fastptr.next is not None:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if slowptr == fastptr:
                return 1
        return 0
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reverseKGroup(self, head, k):
        # split into groups
        groups = []
        cur = head

        while cur:
            start, count = cur, 1
            while count < k and cur.next:
                cur = cur.next
                count += 1

            groups.append((start, count == k))
            nxt = cur.next
            cur.next = None
            cur = nxt
        
        # reverse
        heads = [self.reverse(head) if full else head for head, full in groups]

        # merge

        dummy = ListNode()
        tail = dummy

        for head in heads:
            tail.next = head
            while tail.next:
                tail = tail.next

        return dummy.next


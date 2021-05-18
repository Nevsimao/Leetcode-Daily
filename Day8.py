# Intersection of Two Linked Lists

## Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

### Solution (Python)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:
            if not a: a = headB
            else: a = a.next
            if not b: b = headA
            else: b = b.next
        return a

# Odd Even Linked List

## Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

### Solution (Python)

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd, even = ListNode(0), ListNode(0)
        oddHead, evenHead = odd, even
        current = 0
        
        while head:
            if current & 1 == 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            current += 1
        even.next = None
        odd.next = evenHead.next
        
        return oddHead.next

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        while l1 or l2 or carry:
            val1 = (l1.value if l1 else 0)
            val2 = (l2.value if l2 else 0)
            sum = val1 + val2 + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummyHead.next 


def list_to_linkedlist(elements: list) -> Optional[ListNode]:
    head = ListNode(0)  # Dummy head
    current = head
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return head.next

if __name__ == "__main__":
    
    l1_list = [2,4,3]
    l2_list = [5,6,4]
    l1_linked = list_to_linkedlist(l1_list)
    l2_linked = list_to_linkedlist(l2_list)

    sol = Solution()
    res = sol.add_two_numbers(l1_linked, l2_linked)

    current = res
    while current:
        print(current.value, end=" ")
        current = current.next
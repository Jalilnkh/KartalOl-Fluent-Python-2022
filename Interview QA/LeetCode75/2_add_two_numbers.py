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
        
        # Loop until both lists are fully traversed and there's no carry left
        while l1 or l2 or carry:
            # If l1 or l2 is not None, get its value; otherwise, use 0
            val1 = (l1.value if l1 else 0)
            val2 = (l2.value if l2 else 0)
            
            # Calculate the sum of values and carry
            sum = val1 + val2 + carry
            
            # Update carry for the next iteration
            carry = sum // 10
            
            # Create a new node with the last digit of the sum and set it as the next of current node
            current.next = ListNode(sum % 10)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they are not None
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the head of the newly formed list, skipping the dummy head
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
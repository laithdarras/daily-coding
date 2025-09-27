"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. 
The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""

# UNDERSTAND
# This problem involves adding two whole numbers represented as linked lists in reverse order and adding them together to return
# another linked list in reverse order.
# Edge cases: If empty -> return 0. If one list if longer than the other -> treat missing node as 0.
# If the sum of two digits is >= 10, we need to carry over the 1 to the next digit.
# If there's a carry left after the sum is computed, then we need to add a new node to hold that carry value
# The list is in reverse order, so we can start adding from the head of the list with the insert operation.


# MATCH
# This calls for a linked list traversal with an addition operation.



# PLAN
# Create a linked list node class to hold the digit and a pointer to the next node
# Create a function that takes two linked lists as input
# Initialize a new linked list to hold the result
# Initialize a carry variable to hold any carry-over 1
# Traverse both lists at the same time, adding corresponding digits and the carry
# If the sum if >= 10, set carry to 1 and the digit to sum mod 10 for the new node because we only want the last digit
# If one list is shorter, treat the missing node as 0
# Return result

# IMPLEMENT

class LinkedListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_linked_lists(l1, l2):
    head = None
    tail = None
    carry = 0

    while l1 or l2 or carry: # this runs until both lists are processed and there's no carry left
        if l1:
            digit1 = l1.value
            l1 = l1.next
        else:
            digit1 = 0
        if l2:
            digit2 = l2.value
            l2 = l2.next
        else:
            digit2 = 0
        
        res = digit1+ digit2 + carry
        carry = res // 10 # Carry will be 1 if res is >= 10, else 0

        newDigit = res % 10 # We only want the last digit for the new node

        newNode = LinkedListNode(newDigit)

        # This is to insert the new node at the end of the result list
        if not head:
            head = newNode
            tail = newNode
        else:   # Insert at end if head exists
            tail.next = newNode
            tail = newNode
        
    return head
    
def printList(node):
    while node:
        if node.next:
            print(node.value, end=" -> ")
        else:
            print(node.value)
        node = node.next


printList(add_linked_lists(LinkedListNode(9, LinkedListNode(9)), LinkedListNode(5, LinkedListNode(2))))
printList(add_linked_lists(LinkedListNode(1, LinkedListNode(2, LinkedListNode(3))), LinkedListNode(4, LinkedListNode(5, LinkedListNode(6)))))
printList(add_linked_lists(None, None))

# REVIEW
# After debugging, the code works as expected and handles edge cases
# I was debugging an issue where it was printing a memory address instead of the value, so I added a printList function 
# to traverse the list and print the values
# Another issue was it was printing the last digit only, because the return statement was inside the while loop
# Another issue was that it was return AttributeError because I was trying to access the no value before checking if the node actually existed
# Last one was just a formatting issue so I added the end parameter to print on the same line


# EVALUATE
# This code runs in O(N) where N is the length of list, because we traverse each list once
# Space complexity is also O(N) because we create a new list to hold the result
# An optimization could be to modify one of the input lists to hold the result instead of creating a new list,
# but that would depend on whether that's allowed in the problem contraints but also in-place modification
# is generally not a good idea unless necessary

# This problem was not too difficult, but I had to debug a few issues
# LinkedLists are fun to work with
# LET'S GO!
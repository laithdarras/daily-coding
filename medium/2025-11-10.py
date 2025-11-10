"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""


# I need to sort this linkedlist specifically in O(NLOGN) time and O(1)) space. it needs to be able to handle negative numbers too.
# this is a merge sort algorithm but it needs to be a special type of merge sort that runs in constant space so in-place modification is a must
# this will be a more difficult since it requires some complex operations

# Starting to plan...
# Since this is a recursive merge sort on a LL, always start with the base case being an empty list or a list with one node only
# now to start the algorithm, i need to split the list into half
# To split it in half, i find the midpoint. to find it, i can't index a component direclty in a LL so i need to use the tortoise and hare approach
# i will have one pointer move only 1 step at a time (tortoise) and the other moves 2 steps at a time (hare). then when the hare reaches the end, the tortoise will be at the middle
# now i know where the half is, to split it into two (no new lists) by assigning a prev pointer to the node right before the tortoise
# so the first half starts at the head of the list and the second half starts at tortoise
# next, we recursively sort these two lists before merging them
# merging them in-place requires me to use two pointers. i will use tow pointers to point at the heads of the lists and a tail pointer to build the result
# keep doing it until they have no more components in the lists to the tails. 
# if one still has leftover nodes, just add them to the tail
# merging is done!

# let's code this puppy now

# Initialize a LL
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Two functions are needed, 1. Splitting and recursion, 2. Merging logic

# Merge

def merge(a, b):
    dummy = ListNode(None)  # to store the original start of the merged list to return

    tail = dummy

    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a   # Attach 'a' node next in line
            a = a.next   # Move a fwd
        else:
            tail.next = b
            b = b.next
        
        tail = tail.next # Move tail forward for next iteration

    # Remaining nodes
    if a is not None:
        tail.next = a
    else:
        tail.next = b
    
    return dummy.next

# Sort function

def sortList(head):
    # base case

    if head is None or head.next is None:
        return head
    
    # Find mid and split
    tortoise = head
    hare = head
    prev = None

    while hare and hare.next:
        prev = tortoise
        tortoise = tortoise.next
        hare = hare.next.next

    prev.next = None # Cut list in half

    # Recursively sort
    left = sortList(head)
    right = sortList(tortoise)

    # Merge the two halves
    return merge(left, right)


# Helper function to print
def printList(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

print("Before sorting the LL...")
printList(head)

sorted = sortList(head)
print("After sorting the LL...")
printList(sorted)

# Efficient solution running in O(NLOGN) time and O(1) space. 
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
"""

# UNDERSTAND
# I need to implement a stack using a heap data structure.
# Stack is LIFO, Heap is a priority queue.
# Edge cases: popping from an empty stack will be an error. 

# MATCH
# Since stack is LIFO, the best way to simulate this with a heap is to use a max heap because it gets the largest element first

# PLAN
# Use a counter to keep track of the order of elements pushed
# When pushing an item, push a tuple to the heap
# The tuple is (-counter, item) to update the max heap property
# When popping, pop from the heap and return the item part of the tuple

# IMPLEMENT

import heapq

class StackUsingHeap:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def push(self, item):
        heapq.heappush(self.heap, (-self.counter, item))
        self.counter += 1

    def pop(self):
        if not self.heap:
            return "Error: Stack is empty"
        return heapq.heappop(self.heap)[1]
    

test_stack = StackUsingHeap()
test_stack.push(1)
test_stack.push(2)
print(test_stack.pop())  # Should return 2
print(test_stack.pop())  # Should return 1
print(test_stack.pop())  # Should return error message

# Normal stack runs in O(1) time for push and pop
# Max heap stack runs in O(LOGN) time for push and pop bc of heap properties

# Works great and is efficient. This problem was a good exercise to test my data structure knowledge, good break from algorithmic thinking hehe
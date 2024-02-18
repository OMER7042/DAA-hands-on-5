# This file contains the execution code of Cusotm Data Structures.
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent_node(self, i):
        return (i - 1) >> 1

    def left_node(self, i):
        return (i << 1) + 1

    def right_node(self, i):
        return (i << 1) + 2
    
#Now we build a min heap from the given array.

    def build_min_heap(self, arr):
    
        self.heap = arr
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.min_heapify(i)

#We define a fucntion to Heapify the subtree whose root is index i.
            
    def min_heapify(self, i):

        l = self.left_node(i)
        r = self.right_node(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

# The next function returns the minimum element in the heap.

    def get_minimum(self):
        
        if not self.heap:
            return None
        return self.heap[0]
    
# We here define a function that removes and returns the minimum element from the heap.
    
    def pop_minimum(self):
        
        if not self.heap:
            return None
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self.min_heapify(0)
        return min_val

# This fuction Inserts a new element into the heap while maintaining the heap property.

    def insert_value(self, val):
        
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent_node(i)] > self.heap[i]:
            self.heap[self.parent_node(i)], self.heap[i] = self.heap[i], self.heap[self.parent_node(i)]
            i = self.parent_node(i)



# Define a custom data structure
class CustomDS:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

# First we create a min heap with custom data structures
heap = MinHeap()
heap.build_min_heap([CustomDS(7), CustomDS(3), CustomDS(6)])
print("Min Heap for custom DS:")
for item in heap.heap:
    print(item.value, end=" ")

# Lets insert a new custom data structure into the heap
heap.insert_value(CustomDS(2))
print("\nAfter Inserting 2:")
for item in heap.heap:
    print(item.value, end=" ")

# Get the minimum value in the heap
print("\nMinimum Value:", heap.get_minimum().value)

# Pop the minimum value from the heap
print("Popped Minimum value:", heap.pop_minimum().value)

# Display the updated heap
print("Heap after Popping the minimum value:")
for item in heap.heap:
    print(item.value, end=" ")


    print(item.value, end=" ")


###OUTPUT
C:\Users\OMER>C:/Python311/python.exe "c:/Users/OMER/Desktop/DAA codes/minheap.py"
Min Heap for custom DS:
3 7 6 
After Inserting 2:
2 3 6 7
Minimum Value: 2
Popped Minimum value: 2
Heap after Popping the minimum value:
3 7 6

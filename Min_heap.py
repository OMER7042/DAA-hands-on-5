# A min heap is a binary tree where each node is less than or equal to its children, making the smallest element the root.
# The MinHeap class uses an array to represent the heap structure.
# "get_minimum" returns the smallest element (root) in the heap.
# "pop_minimum" removes and returns the smallest element while preserving the heap property.
# "insert_value" adds a new element while maintaining the heap property.
# I have also used float values with integers as the input to show that it supports various data types.
# I have executed the same code for custom data structues in the file named "minheap_custom_ds.py".


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

# his fuction Inserts a new element into the heap while maintaining the heap property.

    def insert_value(self, val):
        
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent_node(i)] > self.heap[i]:
            self.heap[self.parent_node(i)], self.heap[i] = self.heap[i], self.heap[self.parent_node(i)]
            i = self.parent_node(i)


# Lets implement an example for all the functions we have included.
            
heap = MinHeap()
heap.build_min_heap([12, 16, 4, 1,1.2, 8, 15, 14.1])
print("Min Heap is:", heap.heap) 

#insertion of an element into the heap
heap.insert_value(9)
print("After Inserting 9 :", heap.heap)
  
#printing the minimum value
print("Minimum Value:", heap.get_minimum())  

#popping the least value
print("Popped Minimum value:", heap.pop_minimum()) 

#print back the updated heap
print("Heap after Popping the minimum value:", heap.heap)  



###OUTPUT 
C:\Users\OMER>C:/Python311/python.exe "c:/Users/OMER/Desktop/DAA codes/minheap.py"
Min Heap is: [1, 1.2, 4, 14.1, 12, 8, 15, 16]
After Inserting 9 : [1, 1.2, 4, 9, 12, 8, 15, 16, 14.1]
Minimum Value: 1
Popped Minimum value: 1
Heap after Popping the minimum value: [1.2, 9, 4, 14.1, 12, 8, 15, 16]



